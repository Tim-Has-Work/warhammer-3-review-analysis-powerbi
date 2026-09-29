import sys
import csv
import time

import requests

APP_ID = 1142710
URL = f"https://store.steampowered.com/appreviews/{APP_ID}"
MAX_RETRIES = 5

CSV_FIELDS = [
	"recommendationid",
	"author.steamid",
	"author.num_games_owned",
	"author.num_reviews",
	"author.playtime_forever",
	"author.playtime_last_two_weeks",
	"author.playtime_at_review",
	"author.deck_playtime_at_review",
	"author.last_played",
	"language",
	"review",
	"timestamp_created",
	"timestamp_updated",
	"voted_up",
	"votes_up",
	"votes_funny",
	"weighted_vote_score",
	"comment_count",
	"steam_purchase",
	"received_for_free",
	"written_during_early_access",
	"developer_response",
	"timestamp_dev_responded",
	"primarily_steam_deck"
]

def flatten_review( review ):
	# Flatten Steam's nested author data
	author = review.get( "author", {} )

	return {
		"recommendationid": review.get( "recommendationid", "" ),
		"author.steamid": author.get( "steamid", "" ),
		"author.num_games_owned": author.get( "num_games_owned", "" ),
		"author.num_reviews": author.get( "num_reviews", "" ),
		"author.playtime_forever": author.get( "playtime_forever", "" ),
		"author.playtime_last_two_weeks": author.get( "playtime_last_two_weeks", "" ),
		"author.playtime_at_review": author.get( "playtime_at_review", "" ),
		"author.deck_playtime_at_review": author.get( "deck_playtime_at_review", "" ),
		"author.last_played": author.get( "last_played", "" ),
		"language": review.get( "language", "" ),
		"review": review.get( "review", "" ),
		"timestamp_created": review.get( "timestamp_created", "" ),
		"timestamp_updated": review.get( "timestamp_updated", "" ),
		"voted_up": review.get( "voted_up", "" ),
		"votes_up": review.get( "votes_up", "" ),
		"votes_funny": review.get( "votes_funny", "" ),
		"weighted_vote_score": review.get( "weighted_vote_score", "" ),
		"comment_count": review.get( "comment_count", "" ),
		"steam_purchase": review.get( "steam_purchase", "" ),
		"received_for_free": review.get( "received_for_free", "" ),
		"written_during_early_access": review.get( "written_during_early_access", "" ),
		"developer_response": review.get( "developer_response", "" ),
		"timestamp_dev_responded": review.get( "timestamp_dev_responded", "" ),
		"primarily_steam_deck": review.get( "primarily_steam_deck", "" )
	}

def main():
	# Get output CSV from command line
	if len( sys.argv ) != 2:
		raise SystemExit( f"Usage: python {sys.argv[ 0 ]} OUTPUT_CSV" )

	output_file = sys.argv[ 1 ]
	seen_reviews = set()
	total_written = 0

	# Steam review query
	params = {
		"json": 1,
		"filter": "recent",
		"language": "all",
		"review_type": "all",
		"purchase_type": "all",
		"num_per_page": 100,
		"filter_offtopic_activity": 0,
		"cursor": "*"
	}

	with requests.Session() as session:
		with open( output_file, "w", newline = "", encoding = "utf-8" ) as file:
			writer = csv.DictWriter( file, fieldnames = CSV_FIELDS )
			writer.writeheader()

			while True:
				# Fetch next review page immediately
				for attempt in range( MAX_RETRIES ):
					response = session.get( URL, params = params )

					if response.status_code == 429:
						wait_time = int( response.headers.get( "Retry-After", 10 ) )
						print( f"Rate limited. Waiting {wait_time} seconds..." )
						time.sleep( wait_time )
						continue

					try:
						response.raise_for_status()
						break

					except requests.RequestException:
						if attempt == MAX_RETRIES - 1:
							raise

						time.sleep( min( 30, 2 ** ( attempt + 1 ) ) )

				data = response.json()

				if data.get( "success" ) != 1:
					raise RuntimeError( f"Steam API reported failure: {data}" )

				reviews = data.get( "reviews", [] )

				if not reviews:
					break

				new_reviews = 0

				# Write unique reviews
				for review in reviews:
					recommendation_id = review.get( "recommendationid" )

					if not recommendation_id or recommendation_id in seen_reviews:
						continue

					seen_reviews.add( recommendation_id )
					writer.writerow( flatten_review( review ) )

					new_reviews += 1
					total_written += 1

				print( f"Logged {total_written:,} reviews...", end = "\r", flush = True )

				if not new_reviews:
					break

				# Advance Steam cursor
				next_cursor = data.get( "cursor" )

				if not next_cursor or next_cursor == params[ "cursor" ]:
					break

				params[ "cursor" ] = next_cursor

	print( f"\nSaved {total_written:,} reviews to {output_file}" )

if __name__ == "__main__":
	main()

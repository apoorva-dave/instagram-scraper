from insta_scrapper import InstagramScrapper
import argparse
import logging
import os

logging.basicConfig(level=logging.INFO)

def main():

	parser = argparse.ArgumentParser(description='Instagram followers scrapper')
	parser.add_argument('--username', dest='username', action='store')
	parser.add_argument('--password', dest='password', action='store')
	args = parser.parse_args()

	scrapper = InstagramScrapper(args.username, args.password)
	logging.info("Creating session")
	scrapper.create_session()

	logging.info("Extracting followers")
	scrapper.scrape_followers()

	logging.info("Extracting followees")
	scrapper.scrape_following()

	logging.info("Generating unfollowing list. Please check unfollowers text file")
	scrapper.generate_unfollowers_list()

if __name__ == '__main__':
	main()
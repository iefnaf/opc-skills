#!/usr/bin/env python3
"""
Domain overview using DataForSEO API
Usage: python3 scripts/domain_overview.py "example.com"
"""
import argparse
from dataforseo_api import api_post, get_result, format_count


def main():
    parser = argparse.ArgumentParser(description="Domain overview")
    parser.add_argument("domain", help="Target domain")
    parser.add_argument("--location", "-loc", type=int, default=2840,
                        help="Location code (default: 2840 = US)")
    args = parser.parse_args()

    data = [{
        "target": args.domain,
        "location_code": args.location,
        "language_code": "en"
    }]
    
    response = api_post("dataforseo_labs/google/domain_metrics_by_categories/live", data)
    results = get_result(response)
    
    print(f"domain: {args.domain}")
    print(f"location: {args.location}")
    
    if results:
        for result in results:
            metrics = result.get("metrics", {}).get("organic", {})
            print(f"organic_traffic: {format_count(metrics.get('etv'))}")
            print(f"keywords: {format_count(metrics.get('count'))}")
            pos_1 = metrics.get("pos_1", 0)
            pos_2_3 = metrics.get("pos_2_3", 0)
            print(f"top_3_positions: {pos_1 + pos_2_3}")
    else:
        print("No results found")


if __name__ == "__main__":
    main()

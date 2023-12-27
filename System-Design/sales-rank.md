## Sales Rank

- **Description**: Designing a system to list best-selling products overall and by category for a large eCommerce company.
- **Considerations**: System design for ranking products.

## Goal

The goal of this system is to rank products based on sales for a large eCommerce company. The system should be able to provide a list of best-selling products overall and also by category.

## Design Considerations

Data Collection: The system needs to collect sales data for all products. This data can be collected from the order processing system of the eCommerce platform. The sales data needs to be collected in real-time (as each sale occurs)

Data Processing: The sales data needs to be processed to calculate the sales rank of each product. This could be done in real-time (as each sale occurs) or in batches (e.g., every hour or every day depending on how much traffic the eCommerce website gets). Every day would be a great option

Data Storage: The sales rank data needs to be stored in a database that supports fast read operations. This is because the sales rank data will be read frequently but updated relatively infrequently.

Data Presentation: The sales rank data needs to be presented to the users in a user-friendly format. This could be a list of products on the eCommerce website, sorted by sales rank.

Analystics: As Data analystics is often expensive, we should only be concerned about total volumen of sales which could be collected weekly

Scalability: Keeping each category as a seperate pipeline would allow for horizontal scaling. This would allow for the system to scale to handle more categories and more products within each category as they do not depend on each other. We could do an N way merge to get the top N products across all categories.

## Ranking metrics

- Volume of sales: Number of item sales
- Volume of sales per time period: Number of item sales in that category in the last Month/Week/Year
- Ratings: Average rating of the item
- Ratings: Average rating of the item in the last Month/Week
- Weighted score = Average rating + (Item sales / total category sales) \* log(total category sales)
  (The log was added to added to add a sense of proportionality to the weighted score. Without the log, the weighted score would likely be dominated by the nubmer of stars as proportion of market share for a given product is typically quite small)

## Basic implementation

```
class SalesRankSystemByVolume:
    def __init__(self):
        self.sales_data = {}  # Key: product_id, Value: sales_count
        self.rank_data = {}  # Key: category, Value: list of product_ids sorted by sales_count

    def process_sale(self, product_id, category):
        # Update sales data
        if product_id in self.sales_data:
            self.sales_data[product_id] += 1
        else:
            self.sales_data[product_id] = 1

        # Update rank data
        self.rank_data[category] = sorted(self.sales_data.items(), key=lambda item: item[1], reverse=True)

    def get_best_selling_products(self, category):
        return self.rank_data.get(category, [])
```

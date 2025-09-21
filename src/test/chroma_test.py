import chromadb
from chromadb.config import Settings

# client = chromadb.Client(Settings(
#     chroma_db_impl="duckdb+parquet",
#     persist_directory="db/",
# ))
client = chromadb.Client()

# Check if collection already exists, if not create it
try:
    collection = client.get_collection(name="Student")
    print("Collection 'Student' already exists")
except:
    collection = client.create_collection(name="Student")
    print("Created new collection 'Student'")

bill_1 = """
Date: September 15, 2023
To: Jane Doe
Account: 987-654-321
Amount Due: $125.75
Due Date: October 5, 2023
Note: Your electricity bill for the period of August 15 to September 15 is now available. Please pay the amount due by the due date to avoid late fees.
"""

bill_2 = """
Document 2: Telephone Bill
Date: September 20, 2023
To: John Smith
Account: 112-233-445
Amount Due: $65.50
Due Date: October 10, 2023
Note: Your phone bill for the month of September is ready. It includes your monthly service fee and an additional $5 for international calls.
"""

bill_3 = """
Document 3: Car Contract Agreement
Date: September 25, 2023
To: Alex Johnson
Agreement ID: C-7890-ABC
Monthly Payment: $450.00
Due Date: October 15, 2023
Note: Your monthly car payment of $450 is due on October 15. This payment is in accordance with your car lease agreement signed on March 15, 2023.
"""

bill_4 = """
Document 4: Phone Contract Reminder
Date: September 30, 2023
To: Sarah Davis
Contract ID: P-4567-XYZ
Expiration Date: October 30, 2023
Note: Your phone contract is set to expire in 30 days. We'd love to keep you as a customer. Please visit our website or call us to explore renewal options and exclusive deals.
"""

bill_5 = """Document 1: Gym Contract
Date: September 1, 2025
To: Michael Brown
Account: 554433
Monthly Fee: $45.00
Due Date: September 15, 2025
Note: Your monthly gym membership fee is due. Please pay the $45.00 by September 15th to ensure uninterrupted access to all our facilities.
"""

bill_6 = """
Document 2: Appliance Contract
Date: September 10, 2025
To: Emily White
Contract ID: AP-8765-ZYX
Payment: $150.00
Due Date: September 30, 2025
Note: This is a reminder that your next payment for the appliance lease agreement is due. The amount of $150.00 should be paid by September 30th as per your contract.
"""

bill_7 = """
Document 3: Dating Website Contract
Date: September 18, 2025
To: David Lee
Subscription ID: DW-1234-PQR
Renewal Date: October 18, 2025
Note: Your premium subscription to our dating service is set to auto-renew on October 18th for the quarterly fee of $29.99. If you wish to cancel or modify your plan, please do so before this date.
"""

bill_8 = """Gym Membership Agreement
Date: January 10, 2024
To: Liam Parker
Agreement ID: GYM-456-ABC
Monthly Fee: $55.00
Due Date: February 10, 2024
Note: This is a reminder of your monthly gym membership fee of $55.00, which was due on February 10, 2024. Your account is currently overdue. To regain full access to our facilities and avoid a $10 late fee, please make your payment as soon as possible.
"""
bill_9 = """
Document 2: Internet Service Contract
Date: March 5, 2024
To: Olivia Grace
Account: INT-987-XYZ
Monthly Fee: $75.00
Due Date: March 25, 2024
Note: Your monthly internet service payment of $75.00 was due on March 25, 2024. A late fee of $5 has been applied to your account. Your service may be suspended if payment is not received within 72 hours.
"""

bill_10 = """
Document 3: Student Loan Payment
Date: February 12, 2024
To: Noah Carter
Loan ID: SL-123-JKL
Payment: $150.00
Due Date: February 28, 2024
Note: Your scheduled student loan payment of $150.00 was due on February 28, 2024. Please submit your payment to bring your account back to good standing and avoid any further penalties.
"""

bill_11 = """
Document 4: Car Lease Agreement
Date: April 1, 2024
To: Ava Thompson
Agreement ID: CAR-567-MNO
Monthly Payment: $380.00
Due Date: April 20, 2024
Note: Your car lease payment of $380.00 was due on April 20, 2024. This payment is for the period of April. Please be advised that late payments may affect your credit score as outlined in your lease agreement.
"""

bill_12 = """
Document 5: Utility Bill
Date: May 10, 2024
To: Mason Evans
Account: UTIL-345-PQR
Amount Due: $210.50
Due Date: May 30, 2024
Note: Your utility bill for gas and electricity for the month of May was due on May 30, 2024. The total outstanding amount is $210.50. Please pay this amount immediately to prevent service disruption.
"""

bill_13 = """
Document 6: Home Rental Agreement
Date: June 1, 2024
To: Isabella King
Lease ID: RENT-789-STU
Monthly Rent: $1,500.00
Due Date: June 5, 2024
Note: Your rent payment of $1,500.00 for the month of June was due on June 5, 2024. A late fee of $75 has been added to your balance. Please make your payment as soon as possible to avoid further action.
"""

bill_14 = """
Document 7: Credit Card Statement
Date: July 15, 2024
To: James Wright
Account: CC-112-VWX
Minimum Payment: $50.00
Due Date: August 5, 2024
Note: Your credit card statement with a minimum payment of $50.00 was due on August 5, 2024. Failing to make this payment may result in additional fees and a negative impact on your credit history.
"""

bill_15 = """
Document 8: Phone Contract Renewal
Date: August 1, 2024
To: Mia Scott
Contract ID: P-445-YZA
Expiration Date: August 25, 2024
Note: Your phone contract expired on August 25, 2024. Your service has been placed on a month-to-month plan. To get a better rate and new device options, please contact us to renew your contract.
"""

bill_16 = """
Document 9: Home Security Agreement
Date: September 1, 2024
To: Ethan Harris
Agreement ID: SEC-998-BCD
Monthly Fee: $45.00
Due Date: September 15, 2024
Note: Your monthly home security fee of $45.00 was due on September 15, 2024. Your service is at risk of being suspended. Please pay the outstanding balance immediately.
"""

bill_17 = """
Document 10: Mortgage Payment
Date: October 1, 2024
To: Charlotte Green
Loan ID: MORT-776-EFG
Payment: $1,250.00
Due Date: October 10, 2024
Note: Your mortgage payment of $1,250.00 was due on October 10, 2024. Please be aware that late payments can lead to significant fees and negatively affect your home loan agreement.
"""

bill_18 = """
Document 11: Rent Payment
Date: November 1, 2024
To: Liam Parker
Lease ID: RENT-789-STU
Payment: $1,500.00
Due Date: November 5, 2024
Note: Your rent payment of $1,500.00 for the month of November was due on November 5, 2024. A late fee of $75 has been added to your balance. Please make your payment as soon as possible to avoid further action.
"""

bill_19 = """
Document 12: Rent Payment
Date: December 1, 2025
To: Liam Parker
Lease ID: RENT-790-STU
Payment: $1,575.00
Due Date: December 5, 2024
Note: Your rent payment of $1,575.00 for the month of December was due on December 5, 2024. A late fee of $75 has been added to your balance. Please make your payment as soon as possible to avoid further action.
"""

bill_20 = """
Document 13: Rent Payment
Date: January 1, 2025
To: Liam Parker
Lease ID: RENT-791-STU
Payment: $1,650.00
Due Date: January 5, 2025
Note: Your rent payment of $1,650.00 for the month of January was due on January 5, 2025. A late fee of $75 has been added to your balance. Please make your payment as soon as possible to avoid further action.
"""

bill_21 = """
Document 14: Rent Payment
Date: February 1, 2025
To: Liam Parker
Lease ID: RENT-792-STU
Payment: $1,725.00
Due Date: February 5, 2025
Note: Your rent payment of $1,725.00 for the month of February was due on February 5, 2025. A late fee of $75 has been added to your balance. Please make your payment as soon as possible to avoid further action.
"""

# Check if collection is empty before adding documents
if collection.count() == 0:
    print("Adding documents to collection...")
    collection.add(
        documents=[bill_1, bill_2, bill_3, bill_4, bill_5, bill_6, bill_7, bill_8, bill_9, bill_10, bill_11, bill_12, bill_13, bill_14, bill_15, bill_16, bill_17, bill_18, bill_19, bill_20, bill_21],
        metadatas=[
            {"source": "bill_1", "type": "electricity"}, 
            {"source": "bill_2", "type": "phone"}, 
            {"source": "bill_3", "type": "car"}, 
            {"source": "bill_4", "type": "phone"}, 
            {"source": "bill_5", "type": "gym"}, 
            {"source": "bill_6", "type": "appliance"}, 
            {"source": "bill_7", "type": "dating"}, 
            {"source": "bill_8", "type": "gym"}, 
            {"source": "bill_9", "type": "internet"}, 
            {"source": "bill_10", "type": "student loan"}, 
            {"source": "bill_11", "type": "car lease"}, 
            {"source": "bill_12", "type": "utility"}, 
            {"source": "bill_13", "type": "rent"}, 
            {"source": "bill_14", "type": "credit card"}, 
            {"source": "bill_15", "type": "phone"}, 
            {"source": "bill_16", "type": "home security"}, 
            {"source": "bill_17", "type": "mortgage"}, 
            {"source": "bill_18", "type": "rent"},          
            {"source": "bill_19", "type": "rent"},
            {"source": "bill_20", "type": "rent"},
            {"source": "bill_21", "type": "rent"},
        ],
        ids=["bill_1", "bill_2", "bill_3", "bill_4", "bill_5", "bill_6", "bill_7", "bill_8", "bill_9", "bill_10", "bill_11", "bill_12", "bill_13", "bill_14", "bill_15", "bill_16", "bill_17", "bill_18", "bill_19", "bill_20", "bill_21"],
    )
    print(f"Added {collection.count()} documents to collection")
else:
    print(f"Collection already contains {collection.count()} documents, skipping addition")

# you can ask questions of the collection now in natural language
results = collection.query(
    query_texts=["when is liam Parker's rent due?"],
    n_results=2,
)

print(results)

# CrateJoy script for preparing advance shipments

If you are really wanting to just go ahead and assume anyway that every rebill really will go through, it is possible to see the list of such shipments by browsing or exporting the current active subscriber list. We needed to do this when acquiring the anime box FaniPack from the previous owner and needing to complete a shipment earlier as the shipping country changed from USA to Japan and wanting to avoid any delays. Some rebills not going through was a risk we were willing to take to make sure the transition would go smoothly.

This was our process for getting the list of addresses to send to with the assumption that any active subscriber would need to be sent to despite their payment not yet going through.

* Go to CrateJoy’s customer list and filter by the desired product
* Press the upper right green "export" button.
* Choose "CSV - all customers"
* Process the CSV in Excel and then use csv_to_shipping_list.py to filter inactive subscribers and create address list

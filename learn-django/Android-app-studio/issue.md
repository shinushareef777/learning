# Findings

## API
  - The configure endpoint returns invoice data for 2 months when selecting a promotion, due to the presence of the billed_months parameter.
  - Specifically, the API is sending 2 months' worth of invoices, even though the required month is 1. This discrepancy occurs because the parameter is set to 1 when selecting a promotion, but   the code on the router increments it by 1, resulting in a value of 2.
  - The API is sending the number of invoices for the value specified in the billed_months parameter, i.e., it is sending 2 months' worth of invoices, even though the number of required months is 1. 

## UI
 - On the frontend, the end_date and rent are being updated by looping through the received invoice data.
 - On the last iteration, the end_date on the invoice data is that of the 2nd month and that is being updated and displayed as the end_date. 
 - Additionally, during the loop, the rent and other calculations in the summary are continuously added, causing the UI to show data for 2 months instead of the intended single month.
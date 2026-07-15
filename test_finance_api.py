from finance_api import Finance

finance_data = Finance()

# print(finance_data.get_stock_price("MSFT"))

# Analyse the relative strength index of the stock.
analysis = finance_data.get_relative_strength_index_assessment("RPI.L")
# analysis = finance_data.get_relative_strength_index_assessment("MSFT")
# analysis = finance_data.get_relative_strength_index_assessment("MSI")
# analysis = finance_data.get_relative_strength_index_assessment("NVDA")

# Call 'analyse_dip_status' using the 'status' key string ("Up", "Down", or "Flat")
dip_report = finance_data.analyse_dip_status(analysis["status"])

# 4. Call 'create_visual_scale' using the 'rsi' key float number
visual_scale = finance_data.create_visual_scale(analysis["rsi"])




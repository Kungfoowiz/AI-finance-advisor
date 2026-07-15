from finance_api import Finance

def analyse_stock(name: str) -> str:
    # Fetches the 3-month daily RSI data and provides a short-term trading assessment.
    # Args:
        # name: The stock name (e.g., 'MSFT', 'AAPL', or 'RPI.L' for stocks).
        
    # Returns:
        # A text analysis string detailing the index score and market momentum trend.
   
    # Instantiate your underlying class engine
    finance_data = Finance()
    
    # Execute the RSI metric evaluation logic (Returns a dictionary)
    analysis = finance_data.get_relative_strength_index_assessment(name)
    
    # Call 'analyse_dip_status' using the 'status' key string
    dip_report = finance_data.analyse_dip_status(analysis["status"])
    
    # Call 'create_visual_scale' using the 'rsi' key float number
    visual_scale = finance_data.create_visual_scale(analysis["rsi"])
    
    # Combine all components into a single multi-line response for Gemini
    result = (
        f"{analysis['summary']}\n"
        f"{visual_scale}\n"
        f"Trend Insight: {dip_report}"
    )
    
    return result

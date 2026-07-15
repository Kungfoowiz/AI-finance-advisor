import yfinance as finance_api

class Finance:
    def get_full_name(self, stock_name: str) -> str:
        return finance_api.Ticker(stock_name).info.get("longName", "WARNING: Company full name not found.")
    

    def get_stock_price(self, stock_name: str) -> float:
        return finance_api.Ticker(stock_name).fast_info["last_price"]
    

    def get_relative_strength_index_assessment(self, stock_name: str) -> dict:
        stock_data = finance_api.download(stock_name, period="3mo", progress=False)
        
        close_price = stock_data["Close"].squeeze().diff()

        gain = close_price.where(close_price > 0, 0).rolling(9).mean()
        loss = -close_price.where(close_price < 0, 0).rolling(9).mean()

        relative_strength_index = float((100 - (100 / (1 + (gain / loss)))).iloc[-1])

        if relative_strength_index >= 55:
            status = "Up"
        elif relative_strength_index <= 45:
            status = "Down"
        else:
            status = "Flat"
        
        result_text = f"Relative Strength Index (RSI): {self.get_full_name(stock_name)} | {relative_strength_index:.2f} | {status}"
        print(result_text)

        # Return all three components as a dictionary package
        return {
            "summary": result_text,
            "rsi": round(relative_strength_index, 2),
            "status": status
        }
    
    
    # Translates the RSI status into plain English with explicit error safety.
    def analyse_dip_status(self, status: str) -> str:
        if "Up" in status:
            analysis = "The stock is currently on a strong RISE and nearing a peak. High risk of an immediate pullback."
        elif "Down" in status:
            analysis = "The stock is currently in a DIP. It has dropped sharply and is prime for a potential bounce up."
        elif "Flat" in status:
            analysis = "The stock is STEADY. No aggressive rises or dips detected at the moment."
        else:
            analysis = "ERROR: Invalid relative strength index status provided. Unable to analyse the dip status."

        print(analysis)

        return analysis
        

    def create_visual_scale(self, relative_strength_indicator: float) -> str:
        # Constructs a clean 2D scale with an arrow pointer and linear risk.
        risk_pct = abs(relative_strength_indicator - 50) * 2
        if risk_pct > 100: 
            risk_pct = 100.0

        # Create a 20-character flat track
        total_segments = 10
        position = int(relative_strength_indicator / (100 / total_segments))
        if position >= total_segments:
            position = total_segments - 1

        scale_list = ["-"] * total_segments
        scale_list[position] = "▲"  # Clean arrow pointer
        
        # Keep a subtle center mark if the pointer isn't sitting on it
        if position != 5:
            scale_list[5] = "|"

        slider_bar = "".join(scale_list)

        colour_reset = "\033[0m"

        if risk_pct <= 4.0:
            colour = "\033[92m" # green
        elif risk_pct > 4.0 and risk_pct <= 10.0:
            colour = "\033[38;5;208m" # orange
        else:
            colour = "\033[91m" # red

        result = f"Scale: [0% {slider_bar} 100%] | Loss risk estimate {colour}{risk_pct:.1f}%{colour_reset} |"

        print(result)

        return result



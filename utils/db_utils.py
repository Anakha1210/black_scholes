from utils.db_connect import get_db_connection

def save_calculation(spot,strike,r,vol,T,call_price,put_price):
    conn=get_db_connection()
    curr=conn.cursor()
    
    curr.execute(
        "INSERT INTO BlackScholesInputs (StockPrice,StrickPrice,IntrestRate,Volatility,TimeToExpiry) VALUES (%s, %s, %s, %s, %s)",(spot,strike,r,vol,T)
    )
    conn.commit()
    calc_id=cursor.lastrowid
    
    curr.execute(
        "INSERT INTO BlackScholesOutputs (VolatilityShock, StockPriceShock, OptionPrice, IsCall, CalculationId) VALUES (%s, %s, %s, %s, %s)",(0,0,call_price,1,calc_id)
    )
    
    curr.execute("INSERT INTO BlackScholesOutputs (VolatilityShock, StockPriceShock, OptionPrice, IsCall, CalculationId) VALUES (%s, %s, %s, %s, %s)",(0,0,put_price,0,cal_id)
    )
    
    conn.commit()
    curr.close()
    conn.close()



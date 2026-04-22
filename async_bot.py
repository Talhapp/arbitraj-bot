import time
import config
from exchanges import get_binance, get_kucoin
from logger import log_trade
from notifier import send

def calculate_net_profit(amount, buy_price, sell_price, exchange_buy_fee, exchange_sell_fee, transfer_fee):
    """
    Arbitrajın tüm masraflar çıktıktan sonraki net sonucunu hesaplar.
    """
    
    buy_commission = amount * exchange_buy_fee
    net_buy_amount_usdt = amount - buy_commission
    asset_quantity = net_buy_amount_usdt / buy_price
    
    
    gross_sell_revenue = asset_quantity * sell_price
    
    
    sell_commission = gross_sell_revenue * exchange_sell_fee
    net_sell_revenue = gross_sell_revenue - sell_commission
    
    
    net_profit = net_sell_revenue - amount - transfer_fee
    return net_profit

def run_bot():
    try:
        
        binance = get_binance()
        kucoin = get_kucoin()
        
        print("🚀 Borsalara bağlanılıyor ve piyasa verileri yükleniyor...")
        binance.load_markets()
        kucoin.load_markets()
        print("✅ Piyasalar yüklendi. Takip başlatıldı.")

        while True:
            try:
                
                ticker_b = binance.fetch_ticker(config.SYMBOL)
                ticker_k = kucoin.fetch_ticker(config.SYMBOL)

                b_ask = ticker_b.get('ask') # Binance satış fiyatı 
                b_bid = ticker_b.get('bid') # Binance alış fiyatı 
                k_ask = ticker_k.get('ask') # KuCoin satış fiyatı
                k_bid = ticker_k.get('bid') # KuCoin alış fiyatı

                if not all([b_ask, b_bid, k_ask, k_bid]):
                    print("⚠️ Eksik veri alındı, atlanıyor...")
                    time.sleep(1)
                    continue

                
                profit_a = calculate_net_profit(
                    amount=config.TRADE_AMOUNT,
                    buy_price=b_ask,
                    sell_price=k_bid,
                    exchange_buy_fee=config.BINANCE_FEE,
                    exchange_sell_fee=config.KUCOIN_FEE,
                    transfer_fee=config.TRANSFER_FEE
                )

                
                profit_b = calculate_net_profit(
                    amount=config.TRADE_AMOUNT,
                    buy_price=k_ask,
                    sell_price=b_bid,
                    exchange_buy_fee=config.KUCOIN_FEE,
                    exchange_sell_fee=config.BINANCE_FEE,
                    transfer_fee=config.TRANSFER_FEE
                )

                
                if profit_a > config.THRESHOLD:
                    msg = (
                        f"🚨 <b>NET KÂR FIRSATI (B ➡️ K)</b> 🚨\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"💰 <b>Net Kâr:</b> <code>{profit_a:.2f} USDT</code>\n"
                        f"📊 <b>Hacim:</b> {config.TRADE_AMOUNT} USDT\n\n"
                        f"🛒 <b>Binance Alış:</b> <code>{b_ask}</code>\n"
                        f"🛍️ <b>KuCoin Satış:</b> <code>{k_bid}</code>\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"⚠️ <i>Maliyetler (Komisyon + Transfer) düşülmüştür.</i>"
                    )
                    print(f"🔥 Fırsat! Net Kâr: {profit_a:.2f}")
                    send(msg)
                    log_trade(f"B->K | Net Kar: {profit_a:.2f}")

                elif profit_b > config.THRESHOLD:
                    msg = (
                        f"🚨 <b>NET KÂR FIRSATI (K ➡️ B)</b> 🚨\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"💰 <b>Net Kâr:</b> <code>{profit_b:.2f} USDT</code>\n"
                        f"📊 <b>Hacim:</b> {config.TRADE_AMOUNT} USDT\n\n"
                        f"🛒 <b>KuCoin Alış:</b> <code>{k_ask}</code>\n"
                        f"🛍️ <b>Binance Satış:</b> <code>{b_bid}</code>\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"⚠️ <i>Maliyetler (Komisyon + Transfer) düşülmüştür.</i>"
                    )
                    print(f"🔥 Fırsat! Net Kâr: {profit_b:.2f}")
                    send(msg)
                    log_trade(f"K->B | Net Kar: {profit_b:.2f}")
                
                else:
                    
                    print(f"--- Takipte --- | B->K: {profit_a:.2f} USDT | K->B: {profit_b:.2f} USDT", end="\r")

            except Exception as e:
                print(f"\n❌ Döngü Hatası: {e}")
            
            
            time.sleep(1)

    except Exception as e:
        print(f"\n🛑 KRİTİK SİSTEM HATASI: {e}")
    finally:
        print("\nBot durduruldu.")

if __name__ == "__main__":
    try:
        run_bot()
    except KeyboardInterrupt:
        print("\nKullanıcı çıkış yaptı.")
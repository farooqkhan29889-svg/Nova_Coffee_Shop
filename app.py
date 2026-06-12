# import streamlit as st
# from dotenv import load_dotenv
# from datetime import datetime
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

# load_dotenv()
# # ---------- PAGE CONFIGURATION ----------
# st.set_page_config(page_title="Nova Coffee", page_icon="☕", layout="wide")

# # ---------- CUSTOM CSS FOR BETTER LOOK ----------
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #black;
#     }
#     .stChatMessage {
#         background-color: #red;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ---------- HEADER ----------
# st.title("Nova coffe Ai")
# st.caption("Next-Gen AI Assistant - Built by Farooq | Now taking coffee orders!")

# # Add a beautiful coffee image at the top
# st.image("images/coffee.jpg", 
#          caption="☕ Fresh Brewed Coffee Every Day", 
#          use_container_width=True)

# st.subheader("Our coffe menu ☕ ")
# col1,col2,col3 = st.columns(3)

# with col1:
#     st.image("images/cappuccino.jpg",width=200)
#     st.markdown("**Cappuccino** - small : ₹150 ! meduim : ₹200 ! Large : ₹250")
    
# with col2:
#     st.image("images/latte.jpg", width=200)
#     st.markdown("**Latte** -  : ₹150 ! meduim : ₹200 ! Large : ₹250")
    
# with col3:
#     st.image("images/americano.jpg", width=200)
#     st.markdown("**americano** - small : ₹150 ! meduim : ₹200 ! Large : ₹250")

# col4,col5,col6 = st.columns(3)

# with col4:
#     st.image("images/espresso.jpg",width=200)
#     st.markdown("**espresso** - small : ₹150 ! meduim : ₹200 ! Large : ₹250")
    
# with col5:
#     st.image("images/mocha.jpg", width=200)
#     st.markdown("**mocha** - small : ₹150 ! meduim : ₹200 ! Large : ₹250")
    
# with col6:
#     st.image("images/flat-white.jpg", width=200)
#     st.markdown("**flat-white** - small : ₹150 ! meduim : ₹200 ! Large : ₹250")

    

# with st.sidebar:
#     st.subheader("Nova setting")
    
#     ai_model = st.selectbox(
#         "AI Model",
#         ["llama-3.1-8b-instant", "llama-3.2-90b-vision-preview", "mixtral-8x7b-32768"]
#     )
    
#     temperature = st.slider("Temperature", 0.0, 1.0, 0.70, 0.05)
    
#     st.divider()

# # -------------------- MASSEGE  --------------

# if "messege" not in st.session_state:
#     st.session_state.messeges = []
# if "orders" not in st.session_state:
#     st.session_state.orders = []

# total_chet_messeges = len(st.session_state.messeges)
# total_orders = len(st.session_state.orders)

# st.metric("chat messeges", total_chet_messeges)
# st.metric("coffee orders", total_orders)

# st.divider()

# # --------- TIME ----------------

# now = datetime.now()
# st.write((f"📅 Date: {now.strftime('%d %b %Y')}"))
# st.write((f"📅 time: {now.strftime('%I:%M %p')}"))

# st.divider()

#  # Clear buttons
    
# col1,col2 = st.columns(2)
# with col1:
#     if st.button("🗑️ Clear Chat", use_container_width=True):
#         st.session_state.messages = []
#         st.rerun()
# with col2:
#     if st.button("🧾 Clear Orders", use_container_width=True):
#         st.session_state.orders = []
#         st.rerun()
        
# # ---------- CHAT AREA (Your original Nova chat) ----------

# st.subheader("Chet With Nova")

# @st.cache_resource
# def load_llm():
    
#     return ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

# llm = load_llm()
    

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [
#         SystemMessage(content="""You are NOVA, an AI waiter at Nova Coffee Shop.

# Our menu:
# - Latte ☕
# - Americano ☕
# - Cappuccino ☕
# - Espresso ☕
# - Mocha ☕
# - Flat White ☕

# Sizes: Small (₹150), Medium (₹200), Large (₹250)

# Rules:
# 1. When customer asks menu → show all coffees
# 2. When customer asks best → recommend Cappuccino
# 3. When customer wants to order → ask NAME first
# 4. After name → ask SIZE only
# 5. After size → say exactly:
#    ORDER_CONFIRMED: [name] | [coffee] | [size]
# 6. Never ask for information already given
# 7. Be friendly and warm!""")
#     ]
    
# for messege in st.session_state.messeges:
#     with st.chat_message(messege["role"]):
#         st.markdown(messege["content"])
        
# # chet Nova

# if prompt := st.chat_input("Ask Nova Evnry thing"):
#     st.session_state.messeges.append({"role":"user", "content":prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)
        

# # AI response

#     st.session_state.chat_history.append(HumanMessage(content=prompt))   
#     response = llm.invoke(st.session_state.chat_history)
#     ai_reply = response.content

# # Check if NOVA confirmed an order
#     if "ORDER_CONFIRMED:" in ai_reply:
    
#         parts = ai_reply.split("ORDER_CONFIRMED:")[1].strip().split("|")
#         if len(parts) == 3:
#             order = {
#             "order_id": len(st.session_state.orders) + 1,
#             "name": parts[0].strip(),
#             "coffee": parts[1].strip(),
#             "size": parts[2].strip(),
#             "time": datetime.now().strftime("%H:%M"),
#             "status": "confirmed"
#             }
#         st.session_state.orders.append(order)
#         st.success(f"✅ Order #{order['order_id']} confirmed for {order['name']}! ☕")
#         st.balloons()
            
#     st.session_state.chat_history.append(AIMessage(content=ai_reply))
#     with st.chat_message("assistant"):
#         st.markdown(ai_reply)
#     st.session_state.messeges.append({"role": "assistant", "content": ai_reply})

# # ---------- COFFEE ORDER SECTION ----------
# st.divider()

# st.subheader("☕ Nova's Coffee Order")

# with st.form("coffee_order", clear_on_submit=True):
#     col1, col2 = st.columns(2)
    
#     with col1:
#         customer_name = st.text_input("📝 Your name", placeholder="Enter your name")
#         coffee_type = st.selectbox(
#             "☕ Coffee type",
#             ["Latte", "Americano", "Cappuccino", "Espresso", "Mocha", "Flat White"]
#         )
    
#     with col2:
#         size = st.radio("📏 Size", ["Small", "Medium", "Large"], horizontal=True)
#         extras = st.multiselect(
#             "➕ Extras",
#             ["Extra shot", "Vanilla syrup", "Caramel syrup", "Oat milk", "Whipped cream"]
#         )
    
#     special_instructions = st.text_area("📝 Special instructions (optional)", placeholder="E.g., less sugar, extra hot, etc.")
    
#     submitted = st.form_submit_button("✅ Place Order", use_container_width=True, type="primary")
    
#     if submitted and customer_name:
#     # Create order
#         order = {
#             "order_id": len(st.session_state.orders) + 1,
#             "name": customer_name,
#             "coffee": coffee_type,
#             "size": size,
#             "extras": extras if extras else [],
#             "instructions": special_instructions if special_instructions else "None",
#             "time": datetime.now().strftime("%H:%M"),
#             "status": "confirmed",
#             "timestamp": datetime.now()
#         }
        
#  # Save to session state
#         st.session_state.orders.append(order)
        
# #  ---------- SHOW CONFIRMATION --------------

#         st.success(f"✅ **Order #{order['order_id']} confirmed, {customer_name}!**")
# # Build order summary
#         extras_text = ", ".join(extras) if extras else "No extras"
        
#         st.info(f"""
#         **Order Details:**
#         - ☕ {size} {coffee_type}
#         - ➕ Extras: {extras_text}
#         - 📝 Notes: {order['instructions']}
#         - ⏱️ Ready in: 5-7 minutes
#         """)

# # Nova confirmation in chat
#         with st.chat_message("assistant"):
#             st.markdown(f"✅ **Order #{order['order_id']} placed successfully!**\n\n☕ {size} {coffee_type} for **{customer_name}** will be ready in 5-7 minutes.\n\nThank you for choosing Nova Coffee! 🙏")
        
#         st.balloons()
#         st.rerun()
        
#     elif submitted and not customer_name:
#         st.error("Please enter your name befor placing order")
        
# # ---------- DISPLAY CURRENT ORDERS ----------
        
#     if st.session_state.orders:
        
#        st.divider()
#        st.subheader(f"📋 Current Orders ({len(st.session_state.orders)})")
       
#   # Reverse to show newest first
#     for order in reversed(st.session_state.orders[-10:]):  # Show last 10 orders
#         with st.container():
#             col1, col2, col3 = st.columns([3, 2, 1])
#             with col1:
#                 st.write(f"**#{order['order_id']} - {order['name']}**")
#                 st.write(f"☕ {order['size']} {order['coffee']}")
#                 if order['extras']:
#                     st.write(f"➕ {', '.join(order['extras'])}")
#             with col2:
#                 st.write(f"⏱️ Time: {order['time']}")
#                 st.write(f"📌 Status: ✅ {order['status']}")
#             with col3:
#                 if st.button(f"✅ Done #{order['order_id']}", key=f"done_{order['order_id']}"):
#                     order['status'] = "completed"
#                     st.rerun()
#             st.divider()

# # ---------- ORDER ANALYTICS (Simple) ----------
# if len(st.session_state.orders) > 0:
#     st.divider()
#     with st.expander("📊 Today's Analytics"):
#         # Count coffee types
#         coffee_counts = {}
#         for order in st.session_state.orders:
#             coffee = order['coffee']
#             coffee_counts[coffee] = coffee_counts.get(coffee, 0) + 1
        
#         st.write("**Popular coffees today:**")
#         for coffee, count in sorted(coffee_counts.items(), key=lambda x: x[1], reverse=True):
#             st.write(f"- {coffee}: {count} order(s)")
        
#         # Total revenue (example pricing)
#         prices = {"Small": 150, "Medium": 200, "Large": 250}
#         total_revenue = sum(prices[order['size']] for order in st.session_state.orders)
#         st.metric("💰 Estimated Revenue", f"₹{total_revenue}")

# # ---------- FOOTER ----------
# st.divider()
# st.caption("🤖 Nova AI Coffee Assistant | Built with ❤️ by Farooq | © 2026")
    
import streamlit as st
from dotenv import load_dotenv
from datetime import datetime
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

# ── PAGE CONFIG ──
st.set_page_config(page_title="Nova Coffee", page_icon="☕", layout="wide")

# ── SESSION STATE — must be at top before everything ──
if "messeges" not in st.session_state:
    st.session_state.messeges = []

if "orders" not in st.session_state:
    st.session_state.orders = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="""You are NOVA, an AI waiter at Nova Coffee Shop.

Our menu:
- Latte ☕
- Americano ☕
- Cappuccino ☕
- Espresso ☕
- Mocha ☕
- Flat White ☕

Sizes: Small (₹150), Medium (₹200), Large (₹250)

Rules:
1. When customer asks menu → show all coffees
2. When customer asks best → recommend Cappuccino
3. When customer wants to order → ask NAME first
4. After name → ask SIZE only
5. After size → say exactly:
   ORDER_CONFIRMED: [name] | [coffee] | [size]
6. Never ask for information already given
7. Be friendly and warm!""")
    ]

# ── LLM ──
@st.cache_resource
def load_llm():
    return ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

llm = load_llm()

# ── CSS ──
st.markdown("""
<style>
.stApp { background-color: #1a1a2e; color: white; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──
with st.sidebar:
    st.subheader("Nova Settings")
    ai_model = st.selectbox("AI Model", ["llama-3.1-8b-instant", "mixtral-8x7b-32768"])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.70, 0.05)
    st.divider()
    st.metric("Chat Messages", len(st.session_state.messeges))
    st.metric("Coffee Orders", len(st.session_state.orders))
    st.divider()
    now = datetime.now()
    st.write(f"📅 Date: {now.strftime('%d %b %Y')}")
    st.write(f"⏰ Time: {now.strftime('%I:%M %p')}")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messeges = []
            st.session_state.chat_history = [st.session_state.chat_history[0]]
            st.rerun()
    with col2:
        if st.button("🧾 Clear Orders", use_container_width=True):
            st.session_state.orders = []
            st.rerun()

# ── HEADER ──
st.title("Nova Coffee AI ☕")
st.caption("Next-Gen AI Assistant - Built by Farooq | Now taking coffee orders!")
st.image("images/coffee.jpg", caption="☕ Fresh Brewed Coffee Every Day", use_container_width=True)

# ── MENU IMAGES ──
st.subheader("Our Coffee Menu ☕")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/cappuccino.jpg", width=200)
    st.markdown("**Cappuccino** - S:₹150 | M:₹200 | L:₹250")
with col2:
    st.image("images/latte.jpg", width=200)
    st.markdown("**Latte** - S:₹150 | M:₹200 | L:₹250")
with col3:
    st.image("images/americano.jpg", width=200)
    st.markdown("**Americano** - S:₹150 | M:₹200 | L:₹250")

col4, col5, col6 = st.columns(3)
with col4:
    st.image("images/espresso.jpg", width=200)
    st.markdown("**Espresso** - S:₹150 | M:₹200 | L:₹250")
with col5:
    st.image("images/mocha.jpg", width=200)
    st.markdown("**Mocha** - S:₹150 | M:₹200 | L:₹250")
with col6:
    st.image("images/flat-white.jpg", width=200)
    st.markdown("**Flat White** - S:₹150 | M:₹200 | L:₹250")

# ── CHAT AREA ──
st.divider()
st.subheader("Chat With Nova 🤖")

for messege in st.session_state.messeges:
    with st.chat_message(messege["role"]):
        st.markdown(messege["content"])

if prompt := st.chat_input("Ask Nova anything... ☕"):
    # Show user message
    st.session_state.messeges.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    response = llm.invoke(st.session_state.chat_history)
    ai_reply = response.content
    st.session_state.chat_history.append(AIMessage(content=ai_reply))

    # Check if order confirmed
    if "ORDER_CONFIRMED:" in ai_reply:
        parts = ai_reply.split("ORDER_CONFIRMED:")[1].strip().split("|")
        if len(parts) == 3:
            order = {
                "order_id": len(st.session_state.orders) + 1,
                "name": parts[0].strip(),
                "coffee": parts[1].strip(),
                "size": parts[2].strip(),
                "extras": [],
                "instructions": "None",
                "time": datetime.now().strftime("%H:%M"),
                "status": "confirmed"
            }
            st.session_state.orders.append(order)
            st.success(f"✅ Order #{order['order_id']} confirmed for {order['name']}! ☕")
            st.balloons()

    # Show AI reply
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
    st.session_state.messeges.append({"role": "assistant", "content": ai_reply})

# ── ORDER FORM ──
st.divider()
st.subheader("☕ Nova's Coffee Order")

with st.form("coffee_order", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        customer_name = st.text_input("📝 Your name", placeholder="Enter your name")
        coffee_type = st.selectbox("☕ Coffee type", ["Latte", "Americano", "Cappuccino", "Espresso", "Mocha", "Flat White"])
    with col2:
        size = st.radio("📏 Size", ["Small", "Medium", "Large"], horizontal=True)
        extras = st.multiselect("➕ Extras", ["Extra shot", "Vanilla syrup", "Caramel syrup", "Oat milk", "Whipped cream"])
    special_instructions = st.text_area("📝 Special instructions (optional)")
    submitted = st.form_submit_button("✅ Place Order", use_container_width=True, type="primary")

    if submitted and customer_name:
        order = {
            "order_id": len(st.session_state.orders) + 1,
            "name": customer_name,
            "coffee": coffee_type,
            "size": size,
            "extras": extras if extras else [],
            "instructions": special_instructions if special_instructions else "None",
            "time": datetime.now().strftime("%H:%M"),
            "status": "confirmed"
        }
        st.session_state.orders.append(order)
        st.success(f"✅ Order #{order['order_id']} confirmed, {customer_name}!")
        extras_text = ", ".join(extras) if extras else "No extras"
        st.info(f"☕ {size} {coffee_type} | ➕ {extras_text} | ⏱️ Ready in 5-7 minutes")
        st.balloons()
        st.rerun()
    elif submitted and not customer_name:
        st.error("Please enter your name before placing order")

# ── CURRENT ORDERS ──
if st.session_state.orders:
    st.divider()
    st.subheader(f"📋 Current Orders ({len(st.session_state.orders)})")
    for order in reversed(st.session_state.orders[-10:]):
        with st.container():
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.write(f"**#{order['order_id']} - {order['name']}**")
                st.write(f"☕ {order['size']} {order['coffee']}")
            with col2:
                st.write(f"⏱️ Time: {order['time']}")
                st.write(f"📌 Status: ✅ {order['status']}")
            with col3:
                if st.button(f"✅ Done", key=f"done_{order['order_id']}"):
                    order['status'] = "completed"
                    st.rerun()
            st.divider()

# ── ANALYTICS ──
if len(st.session_state.orders) > 0:
    st.divider()
    with st.expander("📊 Today's Analytics"):
        coffee_counts = {}
        for order in st.session_state.orders:
            coffee = order['coffee']
            coffee_counts[coffee] = coffee_counts.get(coffee, 0) + 1
        st.write("**Popular coffees today:**")
        for coffee, count in sorted(coffee_counts.items(), key=lambda x: x[1], reverse=True):
            st.write(f"- {coffee}: {count} order(s)")
        prices = {"Small": 150, "Medium": 200, "Large": 250}
        total_revenue = sum(prices.get(order['size'], 0) for order in st.session_state.orders)
        st.metric("💰 Estimated Revenue", f"₹{total_revenue}")

# ── FOOTER ──
st.divider()
st.caption("🤖 Nova AI Coffee Assistant | Built with ❤️ by Farooq | © 2026")
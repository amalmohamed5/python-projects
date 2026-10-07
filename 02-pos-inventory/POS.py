inventory={
    "milk": {"price": 50, "quntity": 5},
    "bread": {"price": 20, "quntity": 10},
    "chips": {"price": 15, "quntity": 20},
    "water": {"price": 10, "quntity": 10}
}
cart=[]


def show_product():
    for index, (name, details) in enumerate(inventory.items(), start=1):
        print(f"{index}. product: {name} , price: {details['price']} , quntity: {details['quntity']}")
def addto_cart():
    if not inventory:
        print("no product found !")
        return
    product=input("Enter product name : ").strip().lower()
    if product not in inventory:
        print("Product not found in inventory!")
        return
    try:   
     qun=int(input("Enter quntity : "))
    except ValueError:
        print("Please enter a valid number for quantity!")
        return
    if qun<=0 : 
        print("Quantity must be greater than 0!")
        return
    if qun<=inventory[product]['quntity']:
        cart.append({
            'name':product,
            'quntity':qun,
            'price':inventory[product]['price'],
            'total price':inventory[product]['price']*qun,
        })
        inventory[product]['quntity']-=qun
        print("product added to your cart")
    else :
        print(f"Not enough quantity available! Only {inventory[product]['quntity']} available.")

def show_cart() :
    
    print("====== CART ======")
    if not cart :
            print("cart is empty!")
            return
    for index,  item in enumerate(cart, start=1):
            print(f"{index}. product: {item['name']} , price: {item['price']} , quntity: {item['quntity']} ,Total: {item['total price']}")

def calculate_total():
    if not cart :
                print("cart is empty!")
                return
    total=0
    print("====== INVOICE ======")
    for item in cart :
        total+=item['total price']
        print(f"{item['name']}   {item['quntity']} x {item['price']} = {item['total price']}")
        print("---------------------------------")
    
    discount = 0
    if total >= 300:
       discount = total * 10 / 100
    final_total = total - discount  
    print(f"Subtotal = {total}")
    print(f"Discount: {discount}")
    print(f"Total after 10% discount: {final_total}")
def check_out():
     calculate_total()
     if not cart :
          print("cart is empty!")
          return
     
     cart.clear()
while True :
  print("=====MAIN MENU=====")
  print("1.show product")
  print("2.add to cart")
  print("3.show cart")
  print("4.calculate total")
  print("5.check out")
  print("6.EXIT")
  choice=input('choose an option (1-6) : ')
  if choice=='1':
      show_product()
  elif choice=='2':
      addto_cart()
  elif choice=='3':
      show_cart()
  elif choice=='4':
      calculate_total()
  elif choice=='5':
       check_out()
  elif choice=='6':
         print('finished')
         break
  else :
       print('invalid number , try again ')

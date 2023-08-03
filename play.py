data = {
    "amazon.com": {
        "username": "mike.belick@gmail.com",
        "password": "1j$Mz&oA!iD0MeD"
    },
    "facebook.com": {
        "username": "mike.belick@gmail.com",
        "password": "t$7*!tS2e2)G3jxQ"
    },
    "blue.com": {
        "username": "mike002",
        "password": "t$7*!tS2e2)G3OJh"
    },
    "blue.com": {
        "username": "mike009",
        "password": "t$dd))jsdmG3OJh"
    },
}


search_term = "facebook.com"

if search_term in data.keys():
    print(f"Website: {search_term}\nUsername: {data[search_term]['username']}\nPassword: {data[search_term]['password']}")
else:
    print("Ooops!")
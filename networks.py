# a dictionary of all networks prefixes
networks = {
    'mtn': ['0803', '0806', '0706', '0703', '0810', '0813', '0814', '0816', '0903', '0906'],
    'airtel': ['0802', '0808', '0812', '0701', '0708', '0902', '0907', '0901'],
    'glo': ['0805', '0807', '0811', '0705', '0815', '0905'],
    '9-mobile': ['0809', '0817', '0818', '0908', '0909'],
    'visafone': ['0704']
}


prompt = "Enter your phone number: "
phone_number = input(prompt)

def check_number (number):
    for network, prefixes in networks.items():
        for prefix in prefixes:
            if len(number) == 11:
                if number[:4] == prefix:
                    print("You're using the ", network.title(), "network")
            else:
                print("Your number is incorrect. Check and enter again")

print(len(phone_number))    
check_number(phone_number)    




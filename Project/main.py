# Github Profile fetcher
import requests

def fetch_github(username):
    url="https://api.github.com/users/"+username

    try:
        header={"User-Agent":"Ilyan321"}
        response=requests.get(url,headers=header)


        if response.status_code==200:
            data=response.json()
            print("Name:",data.get("name","N/A"))
            print("ID:",data.get("id","N/A"))
            print("Bio:",data.get("bio","N/A"))
            print("Profile URL:",data.get("html_url","N/A"))
            print("Profile Picture URL:",data.get("avatar_url","N/A"))
            print("Public Repos:",data.get("public_repos","N/A"))
            print("Followers:",data.get("followers","N/A"))
            print("Following:",data.get("following","N/A"))
            print("Location:",data.get("location","N/A"))
            print("Company:",data.get("company","N/A"))
        elif response.status_code==404:
            print("404 Error: User not found.")
        else:
            print("Error fetching data. Status code:",response.status_code)
    except Exception as e:
        print("An Error Occured:",e)







while True:
    choice=int(input("1.Fetch Github Profile.\n2.Exit.\nEnter your choice: "))
    if choice==1:

        user=input("Enter Github username: ")
        fetch_github(user)
    elif choice==2:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
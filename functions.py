#All functions should be here


def main():
    pass

# ↓↓↓ Ersalor's workspace ↓↓↓
def list_Neighborhoods(*,is_certain=False,certain_province=None,certain_district=None):
    if is_certain==False:
        
        print("Listing Types;\n"
            "1)Listing neighborhoods in the province\n"
            "2)Listing neighborhoods in the district")
        list_Type=input("Please select the listing type:").strip()
        print()
        while list_Type not in ["1","2"]:
            list_Type=input("Enter a valid option(1 or 2):").strip()
            
        print()
        place=input("Which {} would you like to see?:".format("province" if list_Type=="1" else "district")).strip()
        print()
        district_city=""
        if list_Type=="2":
            district_city=input("Which city is that district in?:") 
            print()
        print("Order types;\n"
            "1)Ascending Order\n"
            "2)Descending Order")
        order_Type=input("Please select the listing type:").strip()
        print()
        while order_Type not in ["1","2"]:
            order_Type=input("Enter a valid option(1 or 2):").strip()
            
    elif is_certain==True:
        list_Type="2"
        order_Type="1"
        place=certain_district
        district_city=certain_province

    #####################################################################    
    def turkish_lower(text):
        return text.replace("I","ı").replace("İ","i").lower()
    #####################################################################

    with open("neighborhoods.txt","r",encoding="utf-8") as file:
        count=0
        neighborhoods=[]
        for line in file:
            count+=1
            parts=line.strip().split(" -> ") #part[0]=> mahalle + il,part[1]=> ilce,part[2]=>il+konum bilgisi
            if len(parts)==3:
                
                neighborhood,province=parts[0].strip().rsplit(" ",1)
                district=parts[1]
                typeparts=parts[2].split("-")
                
                if len(typeparts)==2:
                    centertype=typeparts[1]
                else:
                    centertype=typeparts[0]

            elif(len(parts)==2):
                neighborhood,province=parts[0].rsplit(" ",1)
                typeparts=parts[1].split("-")
                
                if len(typeparts)==2:
                    centertype=typeparts[1]
                else:
                    centertype=typeparts[0]

            converted_neighborhood=turkish_lower(neighborhood)
            converted_province=turkish_lower(province)
            converted_district=turkish_lower(district)
            converted_place=turkish_lower(place)
            converted_district_city=turkish_lower(district_city)
            
            if list_Type=="1": #Province
                if converted_place==converted_province and [neighborhood,district] not in neighborhoods:
                        neighborhoods.append([neighborhood,district])
        
            elif list_Type=="2": #District
                if converted_place==converted_district and converted_district_city==converted_province:
                    if neighborhood not in neighborhoods:
                        neighborhoods.append(neighborhood)
    #####################################################################
    turkish_Alphabet="1 2 3 4 5 6 7 8 9 a b c ç d e f g ğ h ı i j k l m n o ö p r s ş t u ü v y z".split()
    def sorting_rule(list_name):
        text=list_name[0]
        list_of_characters=[]
        for character in text.lower():
            if character in turkish_Alphabet:
                character_index=turkish_Alphabet.index(character)
                list_of_characters.append(character_index)
        return list_of_characters
    #####################################################################    
    if order_Type=="1":
        i=0
        if len(neighborhoods)!=0:
            print("Neighborhoods in '{}':".format(place.capitalize()))
            neighborhoods.sort(key=sorting_rule)
            while i<len(neighborhoods):
                print((f"{i+1}){neighborhoods[i][0]}\t({neighborhoods[i][1]})") if list_Type=="1" else (f"{i+1}){neighborhoods[i]}"))
                i+=1
            print("#"*50)    
            print(f"{len(neighborhoods)} neighborhoods have found in {place.capitalize()}\n")
        else:
            print(f"\nThere is no {'city' if list_Type=='1' else 'district'} named {place.capitalize()} in Turkey.\n")    

    elif order_Type=="2":
        i=0
        if len(neighborhoods)!=0: 
            print("Neighborhoods in '{}':".format(place.capitalize()))
            neighborhoods.sort(key=sorting_rule)
            neighborhoods.reverse()
            while i<len(neighborhoods):
                print((f"{i+1}){neighborhoods[i][0]}\t({neighborhoods[i][1]})") if list_Type=="1" else (f"{i+1}){neighborhoods[i]}"))
                i+=1
            print("#"*50)   
            print(f"{len(neighborhoods)} neighborhoods have found in {place.capitalize()}\n")
        else:
            print(f"\nThere is no {'city' if list_Type=='1' else 'district'} named {place.capitalize()} in Turkey.\n")



# ↓↓↓ Mehmetcan's workspace ↓↓↓

def deleting_Neighborhoods(*,is_certain=False,certain_province=None,certain_district=None,certain_neighborhood=None):
    while True:
        
        with open("neighborhoods.txt","r",encoding="utf-8") as reader:
            rows = reader.readlines()

        if is_certain == False:

            Deleting_province = input("Enter the province of the neighborhood to be deleted : ").strip().replace("ı","I").replace("i","İ").upper()
            Deleting_district = input("Enter the district of the neighborhood to be deleted : ").strip().replace("ı","I").replace("i","İ").upper()
            Deleting_neighborhood = input("Enter the neighborhood to be deleted : ").strip().replace("ı","I").replace("i","İ").upper()

        else:
            Deleting_province=certain_province
            Deleting_district=certain_district
            Deleting_neighborhood=certain_neighborhood

        if Deleting_district == "PROVİNCE CENTER" or Deleting_district == "DİSTRİCT CENTER":
            Deleting_district = Deleting_district.replace("İ","I")

        Deleting = Deleting_neighborhood + " " + Deleting_province + " " + Deleting_district

        with open("neighborhoods.txt","w",encoding="utf-8") as file:
            neighborhoods=[]
            not_found = True
            for row in rows:
                parts=row.strip().split(" -> ")
                if len(parts)==3 :
                    
                    neighborhood,province=parts[0].strip().rsplit(" ",1)
                    district=parts[1]

                elif len(parts)==2 :
                    neighborhood,province=parts[0].rsplit(" ",1)
                    typeparts=parts[1].split("-")

                    if len(typeparts)==2:
                        district=typeparts[1]
                    else:
                        district=typeparts[0]

                Find_neighboorhood = neighborhood + " " + province + " " + district
                if Find_neighboorhood != Deleting:
                    file.write(row)
                else:
                    if is_certain == False:
                        print("Neighborhood has been deleted")
                    not_found = False

        if not_found == True:
            print("Neighborhood not found , try again.")
            if is_certain==True:
                break
        else:
            if is_certain == False:
                list_Neighborhoods(is_certain=True,certain_district=Deleting_district,certain_province=Deleting_province)
            break

def updating_Neighborgoods():
    while True:
        with open("neighborhoods.txt","r",encoding="utf-8") as reader:
            rows = reader.readlines()

        Updating_province = input("Enter the province of the neighborhood to be updated : ").strip().replace("ı","I").replace("i","İ").upper()
        Updating_district = input("Enter the district of the neighborhood to be updated : ").strip().replace("ı","I").replace("i","İ").upper()
        Deleting_neighborhood = input("Enter the old name of the neighborhood : ").strip().replace("ı","I").replace("i","İ").upper()
        Updating_neighborhood = input("Enter the new name of the neighborhood : ").strip().replace("ı","I").replace("i","İ").upper()
        deleting_Neighborhoods(is_certain=True,certain_province=Updating_province,certain_district=Updating_district,certain_neighborhood=Deleting_neighborhood)

        with open("neighborhoods.txt","r",encoding="utf-8") as new_reader:
            new_rows = new_reader.readlines()

        if rows != new_rows:
            break

    #add fonsiyonundan sonra açılacak     
    #adding_neighborhoods(is_certain=True,certain_province=Updating_province,certain_district=Updating_district,certain_neighborhood=Updating_neighborhood)
    print("Neighborhood has been updated")
    print(list_Neighborhoods(is_certain=True,certain_province=Updating_province,certain_district=Updating_district))


# ↓↓↓ Hasan's workspace ↓↓↓



if __name__=="__main__":
    main()
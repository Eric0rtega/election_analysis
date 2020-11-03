# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else: 
#     print("El Paso is not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
#     print(county)

# counties_tuple = ("Arapahoe", "Denver", "Jefferson")

# for i in range(len(counties_tuple)):
#     print(counties_tuple[i])

# for i in len(counties_tuple):
#     print(counties_tuple[i])

# for county in counties_tuple:
#     print(county)

# for county in len(counties_tuple):
#     print(county)

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes of the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of total votes.")

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# candidate_votes = 3345
# total_votes = 23123

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
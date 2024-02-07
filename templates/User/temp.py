# while 1:
#     val = int(input("Enter: "))
#     while val%7 != 0:
#         print("%d is not mul of 7" %val)
#         break
#     else:
#         print("%d is not mul of 7" %val)

# import random
# random.choice((2,3,4))

# quetions = [
#     {'Q': 'Q1. What is your Body Build Type?',
#         'C1': 'Lean/slim', 'C2': 'Medium', 'C3': 'Stout/heavy build'},
#     {'Q': 'Q2. What is your Face size?', 'C1': 'Small',
#         'C2': 'Medium', 'C3': 'Big'},
#     {'Q': 'Q3. What is your face color?', 'C1': 'Brown',
#         'C2': 'Reddish white', 'C3': 'Fair'},
#     {'Q': 'Q4. What is your body capacity?', 'C1': 'Poor',
#         'C2': 'Average', 'C3': 'Incredible'},
#     {'Q': 'Q5. What is your nature of behavior?',
#         'C1': 'Playful', 'C2': 'Aggressive', 'C3': 'Calm minded'},
#     {'Q': 'Q6. What is your favorite season?',
#         'C1': 'Spring', 'C2': 'Winter', 'C3': 'Summer'},
#     {'Q': 'Q7. What is your favorite dishes?',
#         'C1': 'Sweet salty and sour', 'C2': 'Spicy sweet', 'C3': 'Bitter spicy hot'},
#     {'Q': 'Q8. How much is your Grasping power?',
#         'C1': 'poor', 'C2': 'Sharp', 'C3': 'Average/ Good'},
#     {'Q': 'Q9. How is your memorizing ability?',
#         'C1': 'Observant but forgot', 'C2': 'Sharp and clear', 'C3': 'Average/ good'},
#     {'Q': 'Q10. How is your Digestion power?',
#         'C1': 'Sometimes less, sometimes better', 'C2': 'Quick digestion, frequent hunger', 'C3': 'Late digestion'},
#     {'Q': 'Q11. What is your diet capacity?',
#         'C1': 'sometimes poor, sometimes higher', 'C2': 'Medium', 'C3': 'Heavier'},
#     {'Q': 'Q12. What is your body color?',
#         'C1': 'Brownish', 'C2': 'fair, dusky', 'C3': 'Reddish white'},
#     {'Q': 'Q13. What is your hair type?', 'C1': 'Dry, fally',
#         'C2': 'Faster ripping', 'C3': 'Thick, Smooth, Long'},
#     {'Q': 'Q14. What is your Type of your Eyes?',
#         'C1': 'Dry, small', 'C2': 'Shiny, Gray-green', 'C3': 'Big, Lazy, thick eyelids'},
#     {'Q': 'Q15. What is your Type of teeth?',
#         'C1': 'Uneven, Big', 'C2': 'Medium, Pretty', 'C3': 'Even, tender'},
#     {'Q': 'Q16. What is your Stool instinct?',
#         'C1': 'Dry, Tight', 'C2': 'Tender, Spread out', 'C3': 'Excessive, Flimsy'},
#     {'Q': 'Q17. What is your sweat instinct?',
#         'C1': 'Poor', 'C2': 'Excess, Smelly', 'C3': 'Medium'},
#     {'Q': 'Q18. How are your Joints?', 'C1': 'Smaller, Hurting, Noisy',
#         'C2': 'Medium, No Noise', 'C3': 'Bigger, No Noise'},
#     {'Q': 'Q19. How is your sleep?', 'C1': 'Less, Restless',
#         'C2': 'Less, but Restful', 'C3': 'Deep sleep'},
#     {'Q': 'Q20. How are your dreams?', 'C1': 'Scary',
#         'C2': 'Aggressive, Violent', 'C3': 'Peaceful, Lake, River, Sea'},
#     {'Q': 'Q21. How is your skin Type?', 'C1': 'Dry, Rough',
#         'C2': 'Bright, Glorious', 'C3': 'Tender, Soft'},
#     {'Q': 'Q22. How is Your Menstruation (For woman only)?',
#     'C1': 'Less flow, More abdominal pain', 'C2': 'Heavy flow', 'C3': 'Moderate flow'},
#     {'Q': 'Q23. How is your Pulse?', 'C1': 'Snakelike, Feebi',
#         'C2': 'Froglike , Faster', 'C3': 'Gentle, Steady'},
# ]

# from collections import Counter
# dict1={
#     'one' : 2,
#     'two' : 2,
#     'three' : 1
# }
# dict1['three'] += 2
# print(max(dict1), dict1['three'])


# votes = {"user1": "yes", "user2": "no", "user3": "yes",
#         "user4": "no", "user5": "maybe", "user6": "yes"}

# res = Counter(votes.values())

# print(res, res['yes'])

dictA = {'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 3}

print("Given Dictionary :", dictA)

k_v_exchanged = {}

for key, value in dictA.items():
    if value not in k_v_exchanged:
        k_v_exchanged[value] = [key]
    else:
        k_v_exchanged[value].append(key)

# Result
print("New Dictionary:", k_v_exchanged)
print(k_v_exchanged[max(k_v_exchanged.keys())], type(k_v_exchanged[max(
    k_v_exchanged.keys())]), len(k_v_exchanged[max(k_v_exchanged.keys())]))




#analize

# if prakrutict['vata'] > prakrutict['pitta'] and prakrutict['vata'] > prakrutict['kapha']:
#     prakruti['primary'] = 'vata'
# elif prakrutict['pitta'] > prakrutict['vata'] and prakrutict['pitta'] > prakrutict['kapha']:
#     prakruti['primary'] = 'pitta'
# elif prakrutict['kapha'] > prakrutict['vata'] and prakrutict['kapha'] > prakrutict['pitta']:
#     prakruti['primary'] = 'kapha'

# sec = (prakrutict['vata'] + prakrutict['pitta'] +
#         prakrutict['kapha']) - (maxkey + minkey)
# if sec == prakrutict['vata']:
#     prakruti['secondary'] = 'vata'
# elif sec == prakrutict['pitta']:
#     prakruti['secondary'] = 'pitta'
# elif sec == prakrutict['kapha']:
#     prakruti['secondary'] = 'kapha'

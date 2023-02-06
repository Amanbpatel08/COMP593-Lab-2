def main():

    about_me = {'student_id':10292249,
                'full_name':'Aman Bhadreshbhai Patel',
                'pizza_toppings':['BACON','PAPARONI','CUCUMBER'],
                'movies':{'title':[],'genre':[]}}

    about_me['movies']['title'].extend(['fifty shades of gray','american pie','fifty shades of darker','friends with benefits'])
    about_me['movies']['genre'].extend(['sci-fi','action','romance','biography'])

    print_student_name_and_id(about_me)
    print('\n')

    
    print_pizza_toppings(about_me)
    print('\n')

    for toppings in ['ONION','JALEPENO','TOMATOES','PANEER','OLIVES','MASHROOM']:
        add_pizza_toppings(about_me,toppings)
    print_pizza_toppings(about_me)
    print('\n')
    
    print_movie_genres(about_me)
    print('\n')
    print_movie_titles(about_me['movies']['title'])
	
def print_student_name_and_id(about_me):
    first_name=about_me['full_name'].split(' ')[0]
    print(f'My name is {about_me["full_name"]}, but you can call me Mr. {first_name}.\nMy student ID is {about_me["student_id"]}.')


    return
    
def add_pizza_toppings(about_me, toppings):
    
    about_me['pizza_toppings'].append(toppings.lower())
    about_me['pizza_toppings'].sort()
    about_me['pizza_toppings']=[i.lower() for i in about_me['pizza_toppings']]
    return

def print_pizza_toppings(about_me):
    print('My favourite pizza toppings are:')
    for i in about_me['pizza_toppings']:
        print(f'- {i}')
    
    return

def print_movie_genres(about_me):
    replacable_values='and '+ about_me['movies']['genre'][-1]
    about_me['movies']['genre'][-1]=replacable_values
    print(f'I like to watch {", ".join(about_me["movies"]["genre"])}.')
    return 

def print_movie_titles(movie_list):
    movie_list[-1]='and '+movie_list[-1]
    print(f'Some of my favourite movies are {", ".join(movie_list)}.')
    return
    
if __name__ == '__main__':
    main()
























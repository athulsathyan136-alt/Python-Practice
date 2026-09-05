print('='*40)
print('🎬 MOVIE CATALOG')
print('='*40)

movies = [
    {"title": "Inception", "year": 2010, "genre": "Sci-Fi"},
    {"title": "The Dark Knight", "year": 2008, "genre": "Action"},
    {"title": "Interstellar", "year": 2014, "genre": "Sci-Fi"}
]

genres = set()
for movie in movies:
    genres.add(movie["genre"])

print(f'Total movies: {len(movies)}')
print(f'Unique genres: {genres}') 

print('=*40')
print('DISPLAY ALL MOVIES')
print('='*40)

for movie in movies:
    title = movie["title"]
    year = movie["year"]
    genre = movie["genre"]
    print(f'-{title} ({year})- {(genre)}')

print('=*40')
print('ADD A NEW MOVIE')
print('='*40)    

new = input("Enter movie title: ")
mewy =int(input('Enter release year: '))
newg =input('Enter genre: ')

movies.append({'title':new, 'year':mewy,'genre':newg})
genres.add(newg)

print(f"\n'{new}' added sucessfully!")

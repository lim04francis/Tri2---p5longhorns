#Cubism
p1 = {"name":"Les Demoiselles", "date": 1907, "painter":"Pablo Picasso", "genre":"Cubism"}
p2 = {"name":"The Weeping Woman", "date": 1937, "painter":"Pablo Picasso", "genre":"Cubism"}
p3 = {"name":"Girl With Mandolin", "date": 1910, "painter":"Pablo Picasso", "genre":"Cubism"}
p4 = {"name":"Portrait of Ambroise Vollard", "date": 1910, "painter":"Pablo Picasso", "genre":"Cubism"}
p5 = {"name":"Violin and Candlestick", "date": 1910, "painter":"Georges Braque", "genre":"Cubism"}

#Surrealism
p6 = {"name":"Persistence of Memory", "date": 1931, "painter":"Salvaldor Dali", "genre":"Surrealism"}
p7 = {"name":"The Great Masturbator", "date": 1929, "painter":"Salvaldor Dali", "genre":"Surrealism"}
p8 = {"name":"Philosopher's Lamp", "date": 1936, "painter":"Rene Margritte", "genre":"Surrealism"}
p9 = {"name":"The Lovers", "date": 1928, "painter":"Rene Margritte", "genre":"Surrealism"}
p10 = {"name":"Golconda", "date": 1953, "painter":"Rene Margritte", "genre":"Surrealism"}

painting_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
for painting in painting_list:
    print(painting["name"] + "|" + (painting["painter"]) + "|" + str(painting["date"]) + "|" + painting["genre"])


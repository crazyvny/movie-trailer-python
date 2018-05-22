import fresh_tomatoes
import media

thorr = media.movie("Thor:The Rangrok",
                    "This story is about super hero Thor from preventing thei\
                    r world destruction called Rangrok",
                    "https://bit.ly/2wRgEGx",
                    "https://www.youtube.com/watch?v=ue80QwXMRHg&t=61s")

blackpather = media.movie("Black Pather",
                          "This is a story about Wakanda,A most technological\
                           advanced nation on the planet and its protector \
                           called Black Panther",
                          "https://bit.ly/2ECr2qa",
                          "https://www.youtube.com/watch?v=xjDjIWPwcPU&t=5s")

avengersiw = media.movie("Avengers:Infinity War",
                         "As Thanos searching for all infinity stones,The Ave\
                         ngers want to stop him and to prevent the \
                         desctruction of the Universe.",
                         "https://bit.ly/2ITf9la",
                         "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

drstrange = media.movie("Dr Strange",
                        "This story about a talented nuro surgeon who discove\
                        rs himself world is protected by Magic",
                        "https://bit.ly/2HvtQLt",
                        "https://www.youtube.com/watch?v=HSzx-zryEgM")

spidermanhomecoming = media.movie("Spider-Man:Homecoming",
                                  "Peter Parker is exploring the concept of b\
                                  ecoming an Avenger with the help of Tony",
                                  "https://bit.ly/2GBS5Cj",
                                  "https://www.youtube.com/watch?v=U0D3AOldjM\
                                  U&t=1s")

ironmanthree = media.movie("Iron Man:3",
                           "Tony Stark aka Iron-Man wants to take down Killig\
                            who uses his technology to create Human Weapons",
                           "https://bit.ly/2GB5KJP",
                           "https://www.youtube.com/watch?v=YLorLVa95Xo")

movies = [thorr, blackpather, avengersiw, drstrange,
          spidermanhomecoming, ironmanthree]
fresh_tomatoes.open_movies_page(movies)

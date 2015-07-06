"""The media and fresh_tomatoes files are imported so their methods"""
# can be used.
import fresh_tomatoes
import media
"""Each object stores the Title, Storyline, Poster Image, and YouTube Trailer"""

# link for a specific movie.
toy_story = media.Movie("Toy Story",
	"Toy Story film is the life of a child that you apacionanan their toys and" 
	"without the know it, their toys have a life of their own, living several adventures.",
	"http://vignette3.wikia.nocookie.net/doblaje/images/a/a6/"
	"Toystory.jpg/revision/latest?cb=20090904005912&path-prefix=es",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"http://www.khabinh.vn/images/files/avatar-oridginal.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

fast_and_furious = media.Movie("Fast and Furious 7",
	"En la nueva pelicula, Ian Shaw (Statham) busca venganza contra Dominic Toretto" 
	"(Vin Diesel) y su equipo por la muerte de su hermano.",
	"http://onlymotors.com/wp-content/uploads/2014/11/Fast-Furious-7.jpg",
	"https://www.youtube.com/watch?v=Skpu5HaVkOc")

tenacious_d = media.Movie("Tenacious D",
	"La pelicula narra la historia de JB (Jack Black), un adolescente al que le" 
	"gusta el rock y desea tener la mejor banda de rock de la historia, es ahi en donde" 
	"tiene una discusion familiar a causa de que su familia es catolica y su padre (Meat Loaf)"
	"le ordena adorar a Dios mientras el este en su casa.",
	"http://4.bp.blogspot.com/_mORBwh1QJnQ/SqdPGKBGlaI/AAAAAAAAAUE/3556oRdM2E0/s400/"
	"Tenacious-D-The-Pick-of-Destiny-poster.jpg",
	"https://www.youtube.com/watch?v=TXxQFMG86HA")

taken_3 = media.Movie("Taken 3",
	"Despues de una breve visita a su hija, Kim, Bryan Mills se encuentra con su ex esposa," 
	"Leonore. Ella le dice que ella y su marido, Stuart St. John, estan teniendo problemas"
	"maritales, diciendole que quiere dejar todo y fantasea, el le entrega una copia de la llave" 
	"de su dpto.",
	"http://vignette3.wikia.nocookie.net/doblaje/images/e/e8/Tak3n.jpg/revision/latest?cb="
	"20141222194803&path-prefix=es",
	"https://www.youtube.com/watch?v=sym4JVoaAww")

if_i_stay = media.Movie("If I Stay",
	"Mia Hall (Chloe Grace Moretz) pensaba que la decision mas dura a la que se enfrentaria"
	"jamas seria ir detras de sus suenos musicales en la prestigiosa escuela Juilliard o seguir"
	"un camino distinto con el amor de su vida, Adam (Jamie Blackley).",
	"http://1.bp.blogspot.com/-YLioWMfYAlA/VAZvbEuPLqI/AAAAAAAABQI/6REZsymBu6A/s1600/live-"
	"for-love-nuevo-poster-decido-quedarme-L-eRUdjN.jpeg",
	"https://www.youtube.com/watch?v=08RrwZem3M0")

# A list containing each movie object is created.
movies = [toy_story, avatar, fast_and_furious,tenacious_d, if_i_stay, taken_3]

# The HTML is generated using the list of movies and the method from
# the fresh_tomatoes file.
fresh_tomatoes.open_movies_page(movies)
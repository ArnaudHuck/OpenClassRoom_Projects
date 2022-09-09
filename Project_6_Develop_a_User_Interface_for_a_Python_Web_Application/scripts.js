const maxSliderResults = 21; // max number of movies per slider
const imgPerSection = 7; // number of images per slider section
const maxResultPages = 4; // max fetch-result pages
const categoryOrder = "r"; // (a)lphabetic / (r)andom
const catPerLoad = 3; // number of categories at start

// ---------------------------------------------------------------------
//                      Setup Top Movie Head
// ---------------------------------------------------------------------

function createTopMovieHead(movieId) {
    /**
     * Creates the Head Section for the Top Rated Movie.
     */
    movieEndPoint = `titles/${movieId}`;
    fetchData(movieEndPoint).then((movieObject) => {
      let imageContainer = document.createElement("img");
      imageContainer.id = "movieImage";
      imageContainer.src = movieObject.image_url;
  
      let movieTitle = document.createElement("h1");
      movieTitle.innerText = movieObject.title;
  
      let playButton = document.createElement("a");
      playButton.href = "#/";
      playButton.innerHTML = '<p id="playButton">Play</p>';
  
      let description = document.createElement("p");
      description.id = "description";
      description.innerText = movieObject.description;
  
      let topMovieBox = document.querySelector(".movieTitleBox");
      topMovieBox.append(imageContainer, movieTitle, playButton, description);
    });
  }
  
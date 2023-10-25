
const API_KEY = "8bcdeb7a82df79afecac2140c05bda70";
const API_BASE = "https://api.themoviedb.org/3";

const basicFetch = async (endpoint) => {
  const req = await fetch(`${API_BASE}${endpoint}`);
  const json = await req.json();
  return json;
};

export default {
  getHomeList: async () => {
    return [
      {
        slug: "originals",
        title: "Netflix Originals",
        items: await basicFetch(
          `/discover/tv?with_network=213&language=en&api_key=${API_KEY}`
        ),
      },
      {
        slug: "trending",
        title: "Trendings",
        items: await basicFetch(
          `/trending/all/week?language=en&api_key=${API_KEY}`
        ),
      },
      {
        slug: "toprated",
        title: "History",
        items: await basicFetch(
          `/movie/top_rated?language=en&api_key=${API_KEY}`
        ),
      },
      {
        slug: "action",
        title: "Action",
        items: await basicFetch(
          `/discover/movie?with_genres=28&language=en&api_key=${API_KEY}`
        ),
      },
      {
        slug: "comedy",
        title: "Comedy",
        items: await basicFetch(
          `/discover/movie?with_genres=35&language=en&api_key=${API_KEY}`
        ),
      },
      {
        slug: "horror",
        title: "Horror",
        items: await basicFetch(
          `/discover/movie?with_genres=27&language=en&api_key=${API_KEY}`
        ),
      },
      {
        slug: "Romance",
        title: "Romance",
        items: await basicFetch(
          `/discover/movie?with_genres=10749&language=en&api_key=${API_KEY}`
        ),
      },
      {
        slug: "documentary",
        title: "Documentaries",
        items: await basicFetch(
          `/discover/movie?with_genres=99&language=en&api_key=${API_KEY}`
        ),
      },
    ];
  },

  getMovieInfo: async (moveid, type) => {
    let info = {};

    if (moveid) {
      switch (type) {
        case "movie":
          info = await basicFetch(
            `/movie/${moveid}?language=en&api_key=${API_KEY}`
          );
          break;

        case "tv":
          info = await basicFetch(
            `/tv/${moveid}?language=en&api_key=${API_KEY}`
          );
          break;

        default:
          info = null;
          break;
      }
    }

    return info;
  },
};

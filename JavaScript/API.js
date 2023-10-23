const apiCall = async () => {
  const url =
    "https://weatherapi-com.p.rapidapi.com/${xyzabc123}";
  const options = {
    method: "GET",
    headers: {
      "X-RapidAPI-Key": "xyz",
      "X-RapidAPI-Host": "abc",
    },
  };

  try {
    const response = await fetch(url, options);
    const result = await response.text();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
};

apiCall();

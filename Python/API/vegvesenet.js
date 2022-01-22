fetch("https://www.vegvesen.no/trafikkdata/api/", {
  method: "POST",
  headers: { "content-type": "application/json" },
  body: JSON.stringify({
    query: `{
      trafficRegistrationPoints(searchQuery: {roadCategoryIds: [F] }) {
        id
        name
        location {
          coordinates {
            latLon {
              lat
              lon
            }
          }
        }
      }
    }`
  })
})
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
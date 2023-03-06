"use strict";

function initMap() {

  let lat = foodStand["latitude"]
  let lng = foodStand["longitude"]

  const map = new google.maps.Map(document.getElementById("mapDetail"), {
    zoom: 15,
    center: { lat: lat, lng: lng },
    mapTypeId: 'terrain',
    disableDefaultUI: true,

    zoomControl: true,
    zoomControlOptions: {
      position: google.maps.ControlPosition.LEFT_TOP,
    },

    streetViewControl: true,
    streetViewControlOptions: {
      position: google.maps.ControlPosition.LEFT_TOP,
    },
    fullscreenControl: true,
    fullscreenControlOptions: {
      position: google.maps.ControlPosition.LEFT_TOP,
    },
  });

  var infowindow = new google.maps.InfoWindow();

  var marker, i;


  var infowindow = new google.maps.InfoWindow();
  marker = new google.maps.Marker({
    position: new google.maps.LatLng(
      foodStand["latitude"],
      foodStand["longitude"]
    ),
    map: map,
    title: foodStand["name"],
    animation: google.maps.Animation.DROP,
    icon: {
      url: imageUrl,
      // labelOrigin: new google.maps.Point(10, 50),
    },
    label: {
      text: foodStand["name"],
      fontWeight: 'bold',
      fontSize: '15px',
      color: "#2b3e3c",
      className: "marker-label",
    }
  });

  var contentString =
  '<div class="infowindow card">' +
  '<img src="' +
  foodStand["image"] +
  '"class="w-50 card-img-top align-self-center" alt="' +
  foodStand["name"] +
  '"/>' +
  "<b>" +
  '<div class="card-body">' +
  '<h5 class="card-title text-center">' +
  foodStand["name"] +
  "</h5>" +
    '<p class="card-text">' +
    "<b>" +
    foodStand["name"] +
    "</b>, " +
    foodStand["description"] +
    "</p>" +
    '<div class="d-flex justify-content-center">' +
    // '<a href="' +
    // foodStand["slug"] +
    // '" class="btn btn-sm btn-primary mx-1">' +
    // foodStand["name"] +
    '<a href="https://www.google.com/maps/search/?api=1&query=' +
    foodStand["latitude"] +
    "%2C" +
    foodStand["longitude"] +
    '"  class="btn btn-sm btn-primary mx-1" target="_blank">' +
    "Directions" +
    "</div>" +
    "</div>" +
    "</div>";

  google.maps.event.addListener(
    marker,
    "click",
    (function (marker, i) {
      return function () {
        infowindow.setContent(contentString);
        infowindow.open(map, marker);
        toggleBounce(marker)
      };
    })(marker, i)
  );

  function toggleBounce(marker) {
    if (marker.getAnimation() !== null) {
      marker.setAnimation(null);
    } else {
      marker.setAnimation(google.maps.Animation.BOUNCE);
    }
  }


  const trafficLayer = new google.maps.TrafficLayer();
  trafficLayer.setMap(map);

  google.maps.event.addListener(map, "click", function () {
    if (infowindow.getMap() != null) {
      infowindow.close();
    }
  });
}

window.initMap = initMap;

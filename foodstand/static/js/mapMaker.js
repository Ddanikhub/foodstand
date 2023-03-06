"use strict";

function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10.4,
    center: { lat: 40.75, lng: -115.62 },
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

  for (i = 0; i < foodStand.length; i++) {
    var infowindow = new google.maps.InfoWindow();
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(
        foodStand[i]["latitude"],
        foodStand[i]["longitude"]
      ),
      map: map,
      title: foodStand[i]["name"],
      animation: google.maps.Animation.DROP,
      icon: {
        url: imageUrl,
        labelOrigin: new google.maps.Point(10, 50),
      },
      label: {
        text: foodStand[i]["name"],
        fontWeight: 'bold',
        fontSize: '15px',
        color: "#2b3e3c",
        className: "marker-label",
      }
    });

    const contentString =
      '<div class="infowindow card">' +
      '<img src="' +
      foodStand[i]["image"] +
      '"class="w-50 card-img-top align-self-center" alt="' +
      foodStand[i]["name"] +
      '"/>' +
      "<b>" +
      '<div class="card-body">' +
      '<h5 class="card-title text-center">' +
      foodStand[i]["name"] +
      "</h5>" +
      '<p class="card-text">' +
      "<b>" +
      foodStand[i]["name"] +
      "</b>, " +
      foodStand[i]["description"] +
      "</p>" +
      '<div class="d-flex justify-content-center">' +
      '<a href="food_stand/' +
      foodStand[i]["id"] +
      "/" +
      foodStand[i]["slug"] +

      '" class="btn btn-sm btn-primary mx-1">' +
      foodStand[i]["name"] +
      '<a href="https://www.google.com/maps/search/?api=1&query=' +
      foodStand[i]["latitude"] +
      "%2C" +
      foodStand[i]["longitude"] +
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
  }

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

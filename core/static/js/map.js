function init_map(map){
  var mapOptions = {
    center: new google.maps.LatLng(43.64719534917825, -79.39072608947754),
    zoom: 13
  };
  map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

  google.maps.event.addListener(map, 'click', function (e) {
    if (drawing==true){
      var currentPath = polygon.getPath();
      currentPath.push(e.latLng);
    }
  });
  return map;
}
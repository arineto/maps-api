var info_window = null;
var last_polygon = null;

function new_polygon(map, path, border_color, background_color, info_text, editable, draggable){
  var polygonOptions = {
    path: path, 
    strokeColor: border_color,
    strokeWeight: 2,
    fillColor: background_color, 
    fillOpacity: 0.1,
    editable: editable, 
    draggable: draggable
  };
  var polygon = new google.maps.Polygon( polygonOptions );
  polygon.setMap(map);
  
  google.maps.event.addListener(polygon, 'click', function(e){
    if (info_window){
      info_window.setMap(null);
    }
    info_window = new google.maps.InfoWindow();
    info_window.setContent(info_text);
    info_window.setPosition(e.latLng);
    info_window.open(map);

    mark_polygon(polygon);
  });
  return polygon;
}

function get_path_points(array){
  var path_points = "";
  for (i=0; i<array.length; i++){
    path_points+=array[i].toString()+", ";
  }
  return path_points;
}

function mark_polygon(polygon){
    if(last_polygon){
      last_polygon.setOptions({fillOpacity:0.1});
    }
    last_polygon = polygon;
    polygon.setOptions({fillOpacity:0.3});
}
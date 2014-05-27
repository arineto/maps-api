var info_window = null;
var last_polygon = null;

function new_polygon(map, path, color, title, editable, draggable){

  var polygonOptions = {
    path: path, 
    strokeColor: color,
    strokeWeight: 2,
    fillColor: color, 
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
    info_window.setContent(build_info_window_content(title));
    info_window.setPosition(e.latLng);
    info_window.open(map);

    mark_polygon(polygon);
  });
  return polygon;
}

function mark_polygon(polygon){
    if(last_polygon){
      last_polygon.setOptions({fillOpacity:0.1});
    }
    last_polygon = polygon;
    polygon.setOptions({fillOpacity:0.3});
}

function build_info_window_content(info_text){
  var content = info_text;
  return content;
}
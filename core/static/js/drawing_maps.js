var drawing = false;

function start_drawing(){
  polygon = new_polygon(map, new google.maps.MVCArray(), document.getElementById("color").value, document.getElementById("info_text").value, true, true);
  drawing = true;
  document.getElementById("color").disabled = true;
  document.getElementById("start_drawing").disabled = true;
  document.getElementById("info_text").disabled = true;
  document.getElementById("end_drawing").disabled = false;
}

function end_drawing(edit){
  // polygon.setDraggable(false);
  // polygon.setEditable(false);
  // drawing = false;
  // document.getElementById("color").disabled = false;
  // document.getElementById("start_drawing").disabled = false;
  // document.getElementById("info_text").disabled = false;
  // document.getElementById("end_drawing").disabled = true;
  save_map(edit);
}

function get_path_points(array){
  var path_points = "";
  for (i=0; i<array.length; i++){
    path_points+=array[i].toString()+", ";
  }
  return path_points;
}

function save_map(edit){
  document.new_map_form.points.value = get_path_points(polygon.getPath().getArray());
  if (edit=='false'){
    document.getElementById("id_color").value = document.getElementById("color").value;
    document.new_map_form.info_text.value = document.getElementById("info_text").value;
    document.getElementById("info_text").value="";
  }
  document.new_map_form.submit();
}
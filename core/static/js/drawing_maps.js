var drawing = false;
var polygon = null;

function start_drawing(){
  polygon = new_polygon(map, new google.maps.MVCArray(), document.getElementById("border_color").value, document.getElementById("background_color").value, document.getElementById("info_text").value, true, true);
  drawing = true;
  document.getElementById("border_color").disabled = true;
  document.getElementById("background_color").disabled = true;
  document.getElementById("start_drawing").disabled = true;
  document.getElementById("info_text").disabled = true;
  document.getElementById("end_drawing").disabled = false;
}

function end_drawing(){
  polygon.setDraggable(false);
  polygon.setEditable(false);
  drawing = false;
  document.getElementById("border_color").disabled = false;
  document.getElementById("background_color").disabled = false;
  document.getElementById("start_drawing").disabled = false;
  document.getElementById("info_text").disabled = false;
  document.getElementById("end_drawing").disabled = true;
  save_map();
}

function save_map(){
  document.new_map_form.points.value = get_path_points(polygon.getPath().getArray());
  document.new_map_form.border_color.value = document.getElementById("border_color").value;
  document.new_map_form.background_color.value = document.getElementById("background_color").value;
  document.new_map_form.info_text.value = document.getElementById("info_text").value;
  document.getElementById("info_text").value="";
  document.new_map_form.submit();
}
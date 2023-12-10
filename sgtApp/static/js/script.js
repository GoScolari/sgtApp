// function iniciarMap(){
//     var coord = {lat:-33.0329345648865 ,lng: -71.58942190236792};
//     var map = new google.maps.Map(document.getElementById('map'),{
//       zoom: 16,
//       center: coord
//     });

//     var marker = new google.maps.Marker({
//       position: coord,
//       map: map,
//       title :'Vehiculo 1',
//     });
    
// }




function iniciarMap() {
  // Coordenadas para el centro del mapa
  var centroMapa = { lat: -33.6158562592371, lng: -69.97122488090214 };

  // Crea el mapa centrado en la posición predeterminada
  var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: centroMapa
  });

  // Define las coordenadas y títulos de los marcadores
  var marcadores = [
      { lat: -33.6158562592371, lng: -69.97122488090214, titulo: 'Vehiculo 1', icon: "{% static 'images/icono_1.jpg' %}" },
      { lat: -33.61454526647217, lng: -69.99634722948554, titulo: 'Vehiculo 2', icon: '{% static "images/icono_1.jpg" %}' },
      { lat: -33.62022815234513, lng: -69.95939179029251, titulo: 'Vehiculo 3', icon: '{% static "images/icono_1.jpg" %}' }
      // Puedes agregar más coordenadas según sea necesario
  ];

  // Itera sobre el array de marcadores y crea un marcador para cada uno
  for (var i = 0; i < marcadores.length; i++) {
      var marker = new google.maps.Marker({
          position: { lat: marcadores[i].lat, lng: marcadores[i].lng },
          map: map,
          title: marcadores[i].titulo,
        //   icon: marcadores[i].icon // Utiliza el icono personalizado para cada marcador
      });
  }
}


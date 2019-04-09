<script type="text/javascript" src="https://cdn.jsdelivr.net/async/2.4.0/async.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/fermata/0.10.8/fermata.min.js"></script>
    <script type="text/javascript" src="https://js.api.here.com/v3/3.0/mapsjs-core.js"></script>
    <script type="text/javascript" src="https://js.api.here.com/v3/3.0/mapsjs-service.js"></script>
    <script type="text/javascript" src="https://js.api.here.com/v3/3.0/mapsjs-ui.js"></script>
    <script type="text/javascript" src="https://js.api.here.com/v3/3.0/mapsjs-mapevents.js"></script>    
    <script type="text/javascript" charset="UTF-8">
    /**
    * Boilerplate map initialization code starts below:
    */
    var platform = new H.service.Platform({
      'app_id': 'Ige7JOFlW37fkn9EUKIw',
      'app_code': '4-Nu6-kvpkjHtOHrqjwu8A'
    });

    function moveMap(map, _lat, _lng){
      map.setCenter({lat:_lat, lng:_lng});
      map.setZoom(14);
    }
    function initMap() {
      //Step 1: initialize communication with the platform
      var pixelRatio = window.devicePixelRatio || 1;
      var defaultLayers = platform.createDefaultLayers({
        tileSize: pixelRatio === 1 ? 256 : 512,
        ppi: pixelRatio === 1 ? undefined : 320
      });

      //Step 2: initialize a map  - not specificing a location will give a whole world view.
      var map = new H.Map(document.getElementById('map'),
      defaultLayers.normal.map, {pixelRatio: pixelRatio});

      //Step 3: make the map interactive
      // MapEvents enables the event system
      // Behavior implements default interactions for pan/zoom (also on mobile touch environments)
      var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

      // Create the default UI components
      var ui = H.ui.UI.createDefault(map, defaultLayers);
      moveMap(map, 52.5159, 13.3777);
    }
      

      document.getElementById('submit').addEventListener('click', function() {
        submit()
      });

      function submit() {
        
      }
      initMap()
    </script>
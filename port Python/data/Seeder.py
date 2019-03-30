# require 'csv'
# require 'json'
# require 'faraday'
import pandas as pd
import requests as rq

# bandung = CSV.read("bandung_coord.csv");
IUH = pd.read_csv("IUH__coord.csv")

res = rq.get('http://localhost:9200')
# elastic = Faraday.new(:url => 'http://localhost:9200') do |faraday|
#   faraday.request :url_encoded
#   faraday.response :logger
#   faraday.adapter Faraday.default_adapter
# end

# bandung.each do |node|
#   elastic.put do |req|
#     req.url "/bandung/location/#{node[0]}"
#     req.headers['Content-Type'] = 'application/json'
#     req.body = {pin: {location:{lat:node[2].to_f,lon:node[1].to_f}}}.to_json
#   end
# end




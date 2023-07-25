import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable()
export class MediaVariazioneService {

  private API_URL = "http://127.0.0.1:5000/media_variazione";

  constructor(private http: HttpClient) {}

  getData() {
    return this.http.get(this.API_URL);
  }

}
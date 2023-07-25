import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable()
export class ProduttivitaService {

  private API_URL = "http://127.0.0.1:5000/produttivita_pesca";

  constructor(private http: HttpClient) {}

  getProduttivitaPesca() {
    return this.http.get(this.API_URL);
  }

}
import { Component, OnInit } from '@angular/core';
import { ProduttivitaService } from '../produttivita/produttivita.service';
import { MediaVariazioneService } from '../media-variazione/media-variazione.service';


interface Dato {
  anno: any;
  media_variazione: any;
  regione: any;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  data: any [] = [];
  constructor(private mediaVariazioneService: MediaVariazioneService) { }

  ngOnInit(): void {
    this.getData(); 
}


  getData(): void {
    this.mediaVariazioneService.getData().subscribe((data: any) => {
        this.data = data;
      });
  }
  /* prepareChartData() {
    let chartData = {
      labels: [],
      datasets: [{
        data: [],
        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
        hoverBackgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
      }]
    };
  
    this.data.forEach((item: Dato) => {
      chartData.labels.push(item.regione);
      chartData.datasets[0].data.push(item.media_variazione);
    });
  
    return chartData;
  } */
}
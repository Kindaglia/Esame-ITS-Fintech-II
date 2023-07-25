import { Component, OnInit } from '@angular/core';
import { ProduttivitaService } from './produttivita.service';

@Component({
  selector: 'app-produttivita',
  templateUrl: './produttivita.component.html',
  styleUrls: ['./produttivita.component.scss']
})
export class ProduttivitaComponent implements OnInit {

    produttivita:any[] = [];
    constructor(private produttivitaService: ProduttivitaService,){
        
    }

    ngOnInit(): void {
        this.getData(); 
    }


    getData(): void {
      this.produttivitaService.getProduttivitaPesca().subscribe((data: any) => {
          this.produttivita = data;
        });
    }
    

}
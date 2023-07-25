import { Component, OnInit } from '@angular/core';
import { MediaPercentualeService } from './media-percentuale.service';

@Component({
  selector: 'app-media-percentuale',
  templateUrl: './media-percentuale.component.html',
  styleUrls: ['./media-percentuale.component.scss']
})
export class MediaPercentualeComponent implements OnInit {

  data:any[] = [];
  constructor(private mediaPercentualeService: MediaPercentualeService,){
      
  }

  ngOnInit(): void {
      this.getData(); 
  }


  getData(): void {
    this.mediaPercentualeService.getData().subscribe((data: any) => {
        this.data = data;
      });
  }
  

}
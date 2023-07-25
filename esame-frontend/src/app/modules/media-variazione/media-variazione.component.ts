import { Component } from '@angular/core';
import { MediaVariazioneService } from './media-variazione.service';

@Component({
  selector: 'app-media-variazione',
  templateUrl: './media-variazione.component.html',
  styleUrls: ['./media-variazione.component.scss']
})
export class MediaVariazioneComponent {
  data:any[] = [];
  constructor(private mediaVariazioneService: MediaVariazioneService,){
      
  }

  ngOnInit(): void {
      this.getData(); 
  }


  getData(): void {
    this.mediaVariazioneService.getData().subscribe((data: any) => {
        this.data = data;
      });
  }
}

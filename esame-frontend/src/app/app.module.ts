import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PrimeModule } from './prime.module';
import { MenuBarComponent } from './components/menu-bar.component';
import { ProduttivitaComponent } from './modules/produttivita/produttivita.component';
import { ProduttivitaService } from './modules/produttivita/produttivita.service';
import { MediaPercentualeComponent } from './modules/media-percentuale/media-percentuale.component';
import { MediaPercentualeService } from './modules/media-percentuale/media-percentuale.service';
import { MediaVariazioneComponent } from './modules/media-variazione/media-variazione.component';
import { MediaVariazioneService } from './modules/media-variazione/media-variazione.service';
import { HomeComponent } from './modules/home/home.component';

@NgModule({
  declarations: [
    AppComponent, MenuBarComponent,ProduttivitaComponent,MediaPercentualeComponent,MediaVariazioneComponent,HomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    PrimeModule
  ],
  providers: [ProduttivitaService,MediaPercentualeService,MediaVariazioneService],
  bootstrap: [AppComponent]
})
export class AppModule { }

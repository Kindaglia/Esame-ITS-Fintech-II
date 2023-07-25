import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProduttivitaComponent } from './modules/produttivita/produttivita.component';
import { MediaPercentualeComponent } from './modules/media-percentuale/media-percentuale.component';
import { MediaVariazioneComponent } from './modules/media-variazione/media-variazione.component';
import { HomeComponent } from './modules/home/home.component';

const routes: Routes = [
    { path: 'produttivita', component: ProduttivitaComponent },
    { path: 'media-percentuale', component: MediaPercentualeComponent },
    { path: 'media-variazione', component: MediaVariazioneComponent },
    { path: '', component: HomeComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }

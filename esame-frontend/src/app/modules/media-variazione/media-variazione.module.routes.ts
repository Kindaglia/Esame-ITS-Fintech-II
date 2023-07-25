import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { MediaVariazioneComponent } from './media-variazione.component';


const routes: any[] = [
    { path: 'media-percentuale', component: MediaVariazioneComponent }
];

@NgModule({
    exports: [
        RouterModule
    ]
})

export class MediaVariazioneRoutingModule {
    static forChild() {
        return RouterModule.forChild(
            routes
        )
    }
}
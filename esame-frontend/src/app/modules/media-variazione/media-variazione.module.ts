import { PrimeModule } from "src/app/prime.module";
import { NgModule } from "@angular/core";
import { MediaVariazioneComponent } from "./media-variazione.component";
import { MediaVariazioneRoutingModule } from "./media-variazione.module.routes";

const modules: any[] = [
    MediaVariazioneComponent

];

@NgModule({
    declarations: [modules],
    imports: [
        PrimeModule,
        MediaVariazioneRoutingModule.forChild()
    ],
    exports: [MediaVariazioneComponent],
})

export class MediaPercentualeModule {

}

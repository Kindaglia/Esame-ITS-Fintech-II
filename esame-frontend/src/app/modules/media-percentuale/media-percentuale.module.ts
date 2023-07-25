import { PrimeModule } from "src/app/prime.module";
import { NgModule } from "@angular/core";
import { MediaPercentualeComponent } from "./media-percentuale.component";
import { MediaPercentualeRoutingModule } from "./media-percentuale.module.routes";

const modules: any[] = [
    MediaPercentualeComponent

];

@NgModule({
    declarations: [modules],
    imports: [
        PrimeModule,
        MediaPercentualeRoutingModule.forChild()
    ],
    exports: [MediaPercentualeComponent],
})

export class MediaPercentualeModule {

}

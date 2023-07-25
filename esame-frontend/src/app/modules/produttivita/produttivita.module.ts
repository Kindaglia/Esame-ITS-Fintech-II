import { PrimeModule } from "src/app/prime.module";
import { NgModule } from "@angular/core";
import { ProduttivitaRoutingModule } from "./produttivita.module.routes";
import { ProduttivitaComponent } from "./produttivita.component";

const modules: any[] = [
    ProduttivitaComponent

];

@NgModule({
    declarations: [modules],
    imports: [
        PrimeModule,
        ProduttivitaRoutingModule.forChild()
    ],
    exports: [ProduttivitaComponent],
})

export class ProduttivitaModule {

}

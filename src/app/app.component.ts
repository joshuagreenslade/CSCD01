import { Component } from '@angular/core';
import { MembersService } from './services/members.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [MembersService]
})
export class AppComponent {
}

import { Injectable } from '@angular/core';
import {Http, Headers} from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class MembersService {

  members:any;
  constructor(private _http:Http) { }
  getMembers(){
      this.members = this._http.get('assets/data/team.json').map(res => res.json());
      return this.members;
  }

}
